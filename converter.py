import re
import json

class LasConverter :
    def __init__(self,file):
        self.__log = {"version":{},"well":{},"curve":{},"parameter":{},"data" :{},"other":""}
        self.__generated_keys = []
        self.__null_val = None
        self.__has_converted = False
            
        with open(file,"r") as f:
            self.__lines = f.readlines() # read all lines from data

    def __convert(self):
        section = ""
        for line in self.__lines:
            content = {}

            if len(line) <=1 and ord(line)== 10:
                continue
            
            if "#" in line :
                continue
            
            if "~" in line :
                section = self.__get_current_section(line)
                continue

            if section in {"version","well","parameter", "curve"}:

                mnem_end = re.search("[.]{1}",line).end()
                unit_end = mnem_end + re.search("[ ]{1}",line[mnem_end:]).end()
                colon_end = unit_end + re.search("[:]{1}",line[unit_end:]).start()

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



    def __get_current_section(self,line):

        if '~V' in line :
            return 'version'
            
        elif '~W' in line :
            return 'well'

        elif '~C' in line:
            return 'curve'

        elif '~P' in line:
            return 'parameter'

        elif '~A' in line:
            self.__generated_keys = [e.lower() for e in self.__log['curve'].keys()]
            for key in self.__generated_keys:
                #inital all key to empty list
                self.__log['data'][key]=[]

            return 'data'


        else :
            return 'others'

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
    
    def __parse(self,x):
        try:
            x = int(x)
        except ValueError:
            try:
                x = float(x)
            except ValueError:
                pass

        return x



if __name__ == "__main__":
    c = LasConverter("files/sample1.las")
    json_files = c.get_json()


