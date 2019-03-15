
well = {
    'STRT': {'value': 23.622, 'unit': 'M', 'desc': 'START DEPTH'},
    'STOP': {'value': 1522.1713, 'unit': 'M', 'desc': 'STOP DEPTH'},
    'STEP': {'value': 0.1524, 'unit': 'M', 'desc': 'STEP VALUE'},
    'NULL': {'value': None, 'unit': '', 'desc': 'NULL VALUE'},
    'SRVC': {'value': 'SCH', 'unit': '', 'desc': 'Service Company/Logging company'},
    'DATE': {'value': '1/30/2018', 'unit': '', 'desc': 'LAS file Creation Date'},
    'WELL': {'value': 'JPN-A', 'unit': '', 'desc': 'Well Name'},
    'COMP': {'value': 'PT. Pertamina EP', 'unit': '', 'desc': 'Company'},
    'FLD': {'value': 'JEPON', 'unit': '', 'desc': 'Field'},
    'STATE': {'value': 'JAWA TENGA', 'unit': '', 'desc': 'State'},
    'COUNT': {'value': 'Indonesia', 'unit': '', 'desc': 'Country'},
    'LOC': {'value': 'X', 'unit': '', 'desc': 'Location'},
    'LATI': {'value': -6.9952777778, 'unit': '', 'desc': 'Latitude/Northing'},
    'LONG': {'value': 111.5247222222, 'unit': '', 'desc': 'Longitude/Easting'},
    'PDAT': {'value': 'MSL', 'unit': '', 'desc': 'Permanent Datum'},
    'EPDAT': {'value': 0.0, 'unit': '', 'desc': 'Elevation of Permanent Datum'},
    'LGMEA': {'value': 'KB', 'unit': '', 'desc': 'Log Measured from'},
    'APDAT': {'value': 169.0, 'unit': '', 'desc': 'Elevation Above Permanent Datum'},
    'RWS': {'value': -999, 'unit': '', 'desc': 'Def_Rw'},
    'WST': {'value': -999, 'unit': '', 'desc': 'Def_Rwt'},
    'CNTY': {'value': 'OW 700/39', 'unit': '', 'desc': 'County'}
}

parameter = {}

curve = {
    'DEPTH': {'api_code': None, 'unit': 'M', 'desc': 'Depth'},
    'Perm': {'api_code': None, 'unit': 'md', 'desc': 'perm'}
}

data = {
    'depth': [23.622, 23.7744, 23.9268, 24.0792, 24.2316, 24.384],
    'perm': [0.0, 3001.4817, 3001.4556, 3030.4937, 3028.0435, 2960.1401]
}


version = {
    'VERS': {'value': 2.0, 'unit': '', 'desc': 'CWLS LOG ASCII STANDARD - VERSION 2.0'},
    'WRAP': {'value': False, 'unit': '', 'desc': 'SINGLE LINE PER DEPTH STEP'},
    'CREA': {'value': '1/30/2018 12', 'unit': '', 'desc': '24:47 PM'}
}


bytes_list = [
    b'~VERSION INFORMATION\r\n',
    b' VERS.                 2.0 :   CWLS LOG ASCII STANDARD - VERSION 2.0\r\n',
    b' WRAP.                  NO :   SINGLE LINE PER DEPTH STEP\r\n',
    b' CREA.                 1/30/2018 12:24:47 PM\r\n',
    b'#CREATED USING IP VERSION 3.6.2010.102 BY LELY ON 1/30/2018 12:24:47 PM\r\n',
    b'~WELL INFORMATION\r\n',
    b'#MNEM.UNIT       DATA                          DESCRIPTION MNEMONIC\r\n',
    b'#---------      ---------------------------   --------------------------\r\n',
    b' STRT    .M         23.622                   : START DEPTH\r\n',
    b' STOP    .M         1522.1713                 : STOP DEPTH\r\n',
    b' STEP    .M         0.1524                    : STEP VALUE\r\n',
    b' NULL    .      -999.0000                     : NULL VALUE\r\n',
    b' SRVC    .      SCH                           : Service Company/Logging company\r\n',
    b' DATE    .      1/30/2018                     : LAS file Creation Date\r\n',
    b' WELL    .      JPN-A                         : Well Name\r\n',
    b' COMP    .      PT. Pertamina EP              : Company\r\n',
    b' FLD     .      JEPON                         : Field\r\n',
    b' STATE   .      JAWA TENGA                    : State\r\n',
    b' COUNT   .      Indonesia                     : Country\r\n',
    b' LOC     .      X                             : Location\r\n',
    b' LATI    .      -6.9952777778                 : Latitude/Northing\r\n',
    b' LONG    .      111.5247222222                : Longitude/Easting\r\n',
    b' PDAT    .      MSL                           : Permanent Datum\r\n',
    b' EPDAT   .      0.0000                        : Elevation of Permanent Datum\r\n',
    b' LGMEA   .      KB                            : Log Measured from\r\n',
    b' APDAT   .      169.0000                      : Elevation Above Permanent Datum\r\n',
    b' RWS     .      -999                          : Def_Rw\r\n',
    b' WST     .      -999                          : Def_Rwt\r\n',
    b' CNTY    .      OW 700/39                     : County\r\n',
    b'\r\n',
    b'~CURVE INFORMATION\r\n',
    b'#MNEM          UNIT     API CODE   Curve Type Comments\r\n',
    b'#---------- ---------- ----------  ---------- --------\r\n',
    b' DEPTH     .M                    : Depth      \r\n',
    b' Perm      .md                   : perm       \r\n',
    b'\r\n',
    b'\r\n',
    b'\r\n',
    b'~A Log data section\r\n',
    b'#  DEPTH      Perm   \r\n',
    b'  23.6220    0.0000 \r\n',
    b'  23.7744 3001.4817 \r\n',
    b'  23.9268 3001.4556 \r\n',
    b'  24.0792 3030.4937 \r\n',
    b'  24.2316 3028.0435 \r\n',
    b'  24.3840 2960.1401 \r\n',
    b' \r\n',
    b'\r\n',
    b' ~Other  Information Section \r\n',
    b'The log digits for this well were hand digitized from poor half scale log    \r\n',
    b'prints.  This  was  the  best  information  available  at  the  time.  Every attempt should be made to track down the original films. .Dec. 12,1990  John Doe, Petrophysics\r\n'
]
