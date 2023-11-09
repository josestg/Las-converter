## LAS 2.0 Reader and Converter

[![Build Status](https://travis-ci.org/josestg/Las-converter.svg?branch=master)](https://travis-ci.org/josestg/Las-converter)

This package useful for reading and converting the LAS file to python `dict` and `json`.

LAS (Log ASCII Standard) is a structured ASCII file containing log curve data and header information. For more [detail](http://www.cwls.org/wp-content/uploads/2017/02/Las2_Update_Feb2017.pdf).

### LAS File Example

```
~VERSION INFORMATION
 VERS.                 2.0 :   CWLS LOG ASCII STANDARD - VERSION 2.0
 WRAP.                  NO :   SINGLE LINE PER DEPTH STEP
 CREA.                 1/30/2018 12:24:47 PM
#CREATED USING IP VERSION 3.6.2010.102 BY LELY ON 1/30/2018 12:24:47 PM
~WELL INFORMATION
#MNEM.UNIT       DATA                          DESCRIPTION MNEMONIC
#---------      ---------------------------   --------------------------
 STRT    .M         23.6220                   : START DEPTH
 STOP    .M         1522.1713                 : STOP DEPTH
 STEP    .M         0.1524                    : STEP VALUE
 NULL    .      -999.0000                     : NULL VALUE
 SRVC    .      SCH                           : Service Company/Logging company
 DATE    .      1/30/2018                     : LAS file Creation Date
 WELL    .      JPN-A                         : Well Name
 COMP    .      PT. Pertamina EP              : Company
 FLD     .      JEPON                         : Field
 STATE   .      JAWA TENGA                    : State
 COUNT   .      Indonesia                     : Country
 LOC     .      X                             : Location
 LATI    .      -6.9952777778                 : Latitude/Northing
 LONG    .      111.5247222222                : Longitude/Easting
 PDAT    .      MSL                           : Permanent Datum
 EPDAT   .      0.0000                        : Elevation of Permanent Datum
 LGMEA   .      KB                            : Log Measured from
 APDAT   .      169.0000                      : Elevation Above Permanent Datum
 RWS     .      -999                          : Def_Rw
 WST     .      -999                          : Def_Rwt
 CNTY    .      OW 700/39                     : County

~CURVE INFORMATION
#MNEM          UNIT     API CODE   Curve Type Comments
#---------- ---------- ----------  ---------- --------
 DEPTH     .M                    : Depth
 Perm      .md                   : perm

~A Log data section
#  DEPTH      Perm
  23.6220    0.0000
  23.7744 3001.4817
  23.9268 3001.4556
  24.0792 3030.4937
  24.2316 3028.0435
  24.3840 2960.1401

 ~Other  Information Section
The log digits for this well were hand digitized from poor half scale log
prints.  This  was  the  best  information  available  at  the  time.  Every attempt should be made to track down the original films. .Dec. 12,1990  John Doe, Petrophysics

```

see full LAS file [here](https://github.com/josestnggng/Las-converter/blob/master/files/sample3.las).

### Installation

```bash
pip install las-converter
```

### How to use

LAS converter with `file` input. see [here](https://github.com/josestnggng/Las-converter/blob/master/files).

```py
from LAS import Converter

c = Converter() # create converter object

log = c.set_file("file.las") #return LogWrapper

# get section
data      = log.data
version   = log.version
curve     = log.curve
parameter = log.parameter
well      = log.well
other     = log.other

# or get dictionary
log_in_dict = log.get_dict()
# or print on json format and save to disk
log_in_json = log.get_json("outfile_name")
```

### Server app (Flask)

LAS converter with `stream` input. see [here](https://github.com/josestnggng/Las-converter/blob/master/test/expected.py).

```py
# server app for handling upload
from flask import request
from LAS import Converter

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == "POST":
        f = request.files['file']

        # read stream
        stream = f.stream.readlines()

        # code for Las Converter
        c = Converter()
        log  = c.set_stream(stream)

        # or get only assci/data
        data = log.data
```

### Output

##### JSON

```json
(log = {
  "data": {
    "depth": [23.622, 23.7744, 23.9268, 24.0792, 24.2316, 24.384],
    "perm": [0.0, 3001.4817, 3001.4556, 3030.4937, 3028.0435, 2960.1401]
  }
})
```

##### Python dict

see [detail](https://github.com/josestnggng/Las-converter/blob/master/outfile.json).

```py
log.data = {
    'depth': [23.622, 23.7744, 23.9268, 24.0792, 24.2316, 24.384],
    'perm': [0.0, 3001.4817, 3001.4556, 3030.4937, 3028.0435, 2960.1401]
}
```

see [detail](https://github.com/josestnggng/Las-converter/blob/master/test/expected.py).

### Contributors

- [Asido Saputra Sigalingging](https://github.com/asidosaputra)
- [Jose Sitanggang](https://github.com/josestnggng)
