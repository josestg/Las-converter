## LAS 2.0 Reader and Converter to JSON

This package useful for reading and converting the LAS file to python `dict` and `json`.

LAS (Log ASCII Standard) is a structured ASCII file containing log curve data and header information. For more [detail](http://www.cwls.org/wp-content/uploads/2017/02/Las2_Update_Feb2017.pdf).

### Example LAS File

```
~VERSION INFORMATION
 VERS.                 2.0 :   CWLS LOG ASCII STANDARD - VERSION 2.0
 WRAP.                  NO :   SINGLE LINE PER DEPTH STEP
 CREA.                 1/30/2018 12:24:47 PM
```

see full LAS file [here](https://github.com/josestnggng/Las-converter/blob/master/files/sample1.las).

### Installation
```bash
pip install las-converter
```

### How to use

```py
from LAS import LasConverter

c = LasConverter("file.las") # read file las
data_in_dict = c.get_dict() # return a dict
data_in_json = c.get_json() # return json and make new file outfile.json
```

### Contributors

- [Asido Saputra Sigalingging](https://github.com/asidosaputra)
- [Jose Sitanggang](https://github.com/josestnggng)
