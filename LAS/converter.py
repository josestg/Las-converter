import re
import json

class LasConverter :
    def __init__(self):
        self.supported_version = {2.0}
        self.__log = {"version":{},"well":{},"curve":{},"parameter":{},"data" :{},"other":""}
        self.__generated_keys = []
        self.__null_val = None
        self.__has_converted = False

    def set_file(self, file):
        ext = file.rsplit(".", 1)[-1].lower()
        if ext != "las":
            raise Exception("File format no supported!")

        with open(file, "r") as f:
            self.__lines = f.readlines()
            self.__convert()  # read all lines from data
        return self

    def set_stream(self, stream):
        # stream list of bytes
        self.__lines = stream
        self.__convert()
        return self

    @property
    def data(self):
        if not self.__has_converted:
            self.__convert()
        return self.__log["data"]

    def __convert(self):
        section = ""
        rules = {"version", "well", "parameter", "curve"}

        for line in self.__lines:
            content = {}

            if isinstance(line, bytes):
                line = line.decode("utf-8")

            if len(line) <=1 and ord(line)== 10:
                # line just enter or "\n"
                continue
            
            if "#" in line :
                continue
            
            if "~" in line :
                section = self.__get_current_section(line)
                continue

            if section in rules:

                # index of seperator
                mnem_end = re.search("[.]{1}",line).end()
                unit_end = mnem_end + re.search("[ ]{1}",line[mnem_end:]).end()
                colon_end = unit_end + re.search("[:]{1}",line[unit_end:]).start()

                # divide line
                mnem = line[:mnem_end-1].strip()
                unit = line[mnem_end:unit_end].strip()
                data = line[unit_end:colon_end].strip()
                desc = line[colon_end+1:].strip()
                key = 'value'

                if len(data) == 0:
                    data = None

                if section == "well" and mnem == "NULL" :
                    self.__null_val = data
                    data = None

                if section == "curve" :
                    key = "api code"

                if data is not None :
                    if data == "NO" :
                        data = False
                    elif data == "YES":
                        data = True
                    else :
                        data = self.__parse(data)

                content = {
                    key : data,
                    "unit"  : unit,
                    "desc": desc
                }

                self.__log[section][mnem] = content

            elif section == "data":
                content = line.split()
                for k,v in zip(self.__generated_keys,content) :
                    v = float(v) if v != self.__null_val else None
                    self.__log[section][k].append(v)

            elif section == "other":
                prev_content = self.__log["other"]
                self.__log["other"]=str(prev_content).join(str(line).strip())

        self.__has_converted = True

    def get_las_version(self):
        return self.__log["version"]["VERS"]["value"]
            
    def __get_current_section(self,line):

        if '~V' in line :
            return 'version'

        if self.get_las_version() not in self.supported_version:
            raise Exception("Version not supported!")

        if '~W' in line :
            return 'well'

        elif '~C' in line:
            return 'curve'

        elif '~P' in line:
            return 'parameter'

        elif '~A' in line:
            # generate keys of log[data] based on log[curve]
            self.__generated_keys = [e.lower() for e in self.__log['curve'].keys()]
            for key in self.__generated_keys:
                #inital all key to empty list
                self.__log['data'][key]=[]
            return 'data'
        else :
            return 'others'

    def __parse(self, x):
        try:
            x = int(x)
        except ValueError:
            try:
                x = float(x)
            except ValueError:
                pass

        return x

    def get_json(self,out="outfile"):
        out = out +".json"
        if self.__has_converted == False :
            self.__convert()

        with open(out, "w") as f :
            json.dump(self.__log, f, indent=4)

        return json.dumps(self.__log, indent=4)
    
    def get_dict(self):
        if self.__has_converted == False :
            self.__convert()
        return self.__log
    
