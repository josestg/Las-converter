import re
import json

log = {
    "version":{},
    "well":{},
    "curve":{},
    "parameter":{},
    "data" :{

    },
    "other":""
}

generated_keys = []

with open("files/sample2.las") as f :
    lines = f.readlines() # read all lines from data

    section = ""
    for line in lines:
        content = {}

        if len(line) <=1 and ord(line) == 10:
            continue
        if '~V' in line :
            section = "version"
            continue
        if '~W' in line :
            section = "well"
            continue
        if '~C' in line :
            section = "curve"
            continue
        if '~A' in line :
            section = "data"
            generated_keys =[e.lower() for e in log["curve"].keys()]

            for key in generated_keys :
                log[section][key]=[]
            continue
        if '~P' in line :
            section = "parameter"
            continue
        if '~O' in line :
            section = "other"
            continue
        if '#' in line :
            continue


        #####    
        if section == "version":
            mnem_end = re.search("[.]{1}",line).end()
            unit_end = mnem_end + re.search("[ ]{1}",line[mnem_end:]).end()
            colon_end = unit_end + re.search("[:]{1}",line[unit_end:]).start()

            mnem = line[:mnem_end-1].strip()
            unit = line[mnem_end:unit_end].strip()
            data = line[unit_end:colon_end].strip()
            desc = line[colon_end+1:].strip()


            content = {
                "value" : data,
                "unit"  : unit,
                "desc": desc
            }
            log[section][mnem] = content


        elif section == "well":
            mnem_end = re.search("[.]{1}",line).end()
            unit_end = mnem_end + re.search("[ ]{1}",line[mnem_end:]).end()
            colon_end = unit_end + re.search("[:]{1}",line[unit_end:]).start()

            mnem = line[:mnem_end-1].strip()
            unit = line[mnem_end:unit_end].strip()
            data = line[unit_end:colon_end].strip()
            desc = line[colon_end+1:].strip()


            content = {
                "value" : data,
                "unit" : unit,
                "desc": desc
            }
            log[section][mnem] = content

        elif section == "curve":
            mnem_end = re.search("[.]{1}",line).end()
            unit_end = mnem_end + re.search("[ ]{1}",line[mnem_end:]).end()
            colon_end = unit_end + re.search("[:]{1}",line[unit_end:]).start()

            mnem = line[:mnem_end-1].strip()
            unit = line[mnem_end:unit_end].strip()
            data = line[unit_end:colon_end].strip()
            desc = line[colon_end+1:].strip()

            if len(data) <1:
                data = None

            content = {
                "value" : data,
                "unit" : unit,
                "desc": desc
            }
            log[section][mnem] = content
        elif section == "data":
            content = line.split()
            for k,v in zip(generated_keys,content) :
                log[section][k.lower()].append(float(v))

        elif section == "parameter":
            mnem_end = re.search("[.]{1}",line).end()
            unit_end = mnem_end + re.search("[ ]{1}",line[mnem_end:]).end()
            colon_end = unit_end + re.search("[:]{1}",line[unit_end:]).start()

            mnem = line[:mnem_end-1].strip()
            unit = line[mnem_end:unit_end].strip()
            data = line[unit_end:colon_end].strip()
            desc = line[colon_end+1:].strip()


            content = {
                "value" : data,
                "unit" : unit,
                "desc": desc
            }
            log[section][mnem] = content
        elif section == "other" :
            prev_content = log["other"]
            log["other"]=str(prev_content).join(str(line).strip())




    with open("output.json","w") as out :
        json.dump(log, out, indent=4)


