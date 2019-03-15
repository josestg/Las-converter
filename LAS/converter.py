import re
import json

class LogWrapper:
    def __init__(self):
        self.__log = {"version":{},"well":{},"curve":{},"parameter":{},"data" :{},"other":""}
    
    @property
    def data(self): return self.__log["data"]
    @property
    def version(self): return self.version_section["VERS"]["value"]
    @property
    def version_section(self): return self.__log["version"]
    @property
    def well(self): return self.__log["well"]
    @property
    def curve(self): return self.__log["curve"]
    @property
    def parameter(self): return self.__log["parameter"]
    @property
    def other(self): return self.__log["other"]
    
    def add(self,section,mnem,content):
        if section == "data":
            if isinstance(content,list):
                self.__log[section][mnem] = content
            else:
                self.__log[section][mnem].append(content)
        elif section=="other":
            self.__log[section] = self.other + "".join(str(content).strip())
        else:
            self.__log[section][mnem] = content

    def get_json(self,out="outfile"):
        """Write out.json to disk and Return json format."""
        out = out +".json"
        with open(out, "w") as f :
            json.dump(self.__log, f, indent=4)
        return json.dumps(self.__log, indent=4)
    
    def get_dict(self):
        """Return dict({"version":{},"well":{},"curve":{},"parameter":{},"data" :{},"other":""})"""
        return self.__log
    


class Converter():
    
    def __init__(self):
        self.supported_version = {2.0}
        self.__generated_keys = []
        self.__null_val = None
    
    def __str__(self):
        return "Supported LAS Version : {0}".format(self.supported_version)


    def set_file(self,file):
        """Convert file and Return `self`. """
        ext = file.rsplit(".", 1)[-1].lower()
        if ext != "las":            
            raise Exception("File format no supported!")
        with open(file, "r") as f:
            self.__lines = f.readlines()
        return self.__convert()  # read all lines from data

    def set_stream(self,stream):
        """Convert file and Return `self`. """
        self.__lines = stream
        self.__convert()
        return self.__convert()  # read all lines from data

    def __parse(self, x):
        try:
            x = int(x)
        except ValueError:
            try:
                x = float(x)
            except ValueError:
                pass
        return x
    
    def __convert(self):
        section = ""
        rules = {"version", "well", "parameter", "curve"}
        log = LogWrapper()

        for line in self.__lines:
            content = {}

            if isinstance(line, bytes):
                line = line.decode("utf-8").strip()

            # line just enter or "\n"
            if len(line) <= 1 : continue
            # comment
            if "#" in line: continue

            # section
            if "~" in line:
                section = self.__get_current_section(line)

                # get section version first
                if section == "version": continue

                if log.version not in self.supported_version:
                    raise Exception("Version not supported!")

                # generate keys of log[data] based on log[curve]
                if section == "data":                    
                    self.__generated_keys = [e.lower() for e in log.curve.keys()]
                    for key in self.__generated_keys:
                        #inital all key to empty list
                        log.add(section,key,[])

                continue
            
            # unregistered section
            if section is None: continue

            if section in rules:

                # index of seperator
                mnem_end = re.search("[.]{1}", line).end()
                unit_end = mnem_end + re.search("[ ]{1}", line[mnem_end:]).end()
                colon_end = unit_end + re.search("[:]{1}", line[unit_end:]).start()

                # divide line
                mnem = line[:mnem_end-1].strip()
                unit = line[mnem_end:unit_end].strip()
                data = line[unit_end:colon_end].strip()
                desc = line[colon_end+1:].strip()

                # convert empty string ("") to None
                if len(data) == 0: data = None
                if section == "well" and mnem == "NULL":
                    # save standard LAS NULL value
                    self.__null_val = data
                    data = None

                # parse data to type bool or number
                if data is not None:
                    if data == "NO":
                        data = False
                    elif data == "YES":
                        data = True
                    else:
                        data = self.__parse(data)
                
                # dynamic key
                key = "api_code" if section == "curve" else "value"
                content = {
                    key: data,
                    "unit": unit,
                    "desc": desc
                }

                log.add(section,mnem,content)

            elif section == "data":
                content = line.split()
                for k, v in zip(self.__generated_keys, content):
                    v = float(v) if v != self.__null_val else None
                    log.add(section,k,v)

            elif section == "other":
                log.add(section,None,line)

        return log

    def __get_current_section(self,line):
        if '~V' in line : return 'version'
        if '~W' in line: return 'well'
        if '~C' in line: return 'curve'
        if '~P' in line: return 'parameter'
        if '~O' in line: return 'other'
        if '~A' in line: return 'data'
        # ~ Unregistered section
        return None
