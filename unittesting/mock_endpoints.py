__author__ = 'Lorenzo'

from config import _SERVICE

components = [
  {
      "name": "33SD propulsion",
      "minWorkingTemp": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/DegreeCelsius",
        "value": -12
      },
      "uuid": "123",
      "typeOfPropellant": "http://ontology.projectchronos.eu/subsystems/hydrazine",
      "hasMonetaryValue": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/Euro",
        "value": 11015
      },
      "label": "e3349c8fe32d4174a405aeee1e441fad",
      "hasVolume": {
        "type": "http://ontology.projectchronos.eu/subsystems/cubicMillimeters",
        "value": 11
      },
      "maxWorkingTemp": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/DegreeCelsius",
        "value": 42
      },
      "isStandard": "Cubesat",
      "manufacturer": "Chronos",
      "subsystems/hasMass": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/Gram",
        "value": 10
      },
      "type": _SERVICE + "/subsystem/Spacecraft_Propulsion",
      "hasPower": {
        "type": "http://dbpedia.org/data/Watt.ntriples",
        "value": -78
      }
    },
    {
      "name": "136SD primary power",
      "minWorkingTemp": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/DegreeCelsius",
        "value": -42
      },
      "uuid": "124",
      "hasMonetaryValue": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/Euro",
        "value": 8820
      },
      "label": "e3349c8fe32d4174a405aeee1e441fad",
      "hasVolume": {
        "type": "http://ontology.projectchronos.eu/subsystems/cubicMillimeters",
        "value": 41
      },
      "maxWorkingTemp": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/DegreeCelsius",
        "value": 53
      },
      "isStandard": "Cubesat",
      "hasEfficiency": None,
      "manufacturer": "Chronos",
      "hasMass": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/Gram",
        "value": 62
      },
      "type": _SERVICE + "/subsystem/Spacecraft_PrimaryPower",
      "hasPower": {
        "type": "http://dbpedia.org/data/Watt.ntriples",
        "value": 1764
      }
    },
    {
      "name": "191SD command and data",
      "minWorkingTemp": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/DegreeCelsius",
        "value": -19
      },
      "uuid": "125",
      "hasMonetaryValue": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/Euro",
        "value": 4738
      },
      "label": "e3349c8fe32d4174a405aeee1e441fad",
      "hasVolume": {
        "type": "http://ontology.projectchronos.eu/subsystems/cubicMillimeters",
        "value": 39
      },
      "maxWorkingTemp": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/DegreeCelsius",
        "value": 31
      },
      "isStandard": "Cubesat",
      "manufacturer": "Chronos",
      "hasMass": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/Gram",
        "value": 35
      },
      "type": _SERVICE + "/subsystem/Spacecraft_CDH",
      "hasPower": {
        "type": "http://dbpedia.org/data/Watt.ntriples",
        "value": -23
      }
    },
    {
      "name": "111WNT backup power",
      "minWorkingTemp": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/DegreeCelsius",
        "value": -14
      },
      "uuid": "126",
      "hasMonetaryValue": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/Euro",
        "value": 23904
      },
      "label": "e3349c8fe32d4174a405aeee1e441fad",
      "hasVolume": {
        "type": "http://ontology.projectchronos.eu/subsystems/cubicMillimeters",
        "value": 78
      },
      "maxWorkingTemp": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/DegreeCelsius",
        "value": 79
      },
      "isStandard": "Cubesat",
      "manufacturer": "Chronos",
      "hasMass": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/Gram",
        "value": 157
      },
      "type": _SERVICE + "/subsystem/Spacecraft_BackupPower",
      "hasPower": {
        "type": "http://dbpedia.org/data/Watt.ntriples",
        "value": 1494
      }
    },
    {
      "hasVolume": {
        "type": "http://ontology.projectchronos.eu/subsystems/cubicMillimeters",
        "value": 227
      },
      "manufacturer": "Chronos",
      "type": _SERVICE + "/subsystem/Spacecraft_Detector",
      "holdsSensor": "http://ontology.projectchronos.eu/subsystems/MichelsonInterferometer",
      "hasMonetaryValue": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/Euro",
        "value": 2070
      },
      "minWorkingTemp": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/DegreeCelsius",
        "value": -24
      },
      "name": "132T detector",
      "hasPower": {
        "type": "http://dbpedia.org/data/Watt.ntriples",
        "value": -51
      },
      "isStandard": "Cubesat",
      "maxWorkingTemp": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/DegreeCelsius",
        "value": 35.0
      },
      "uuid": "127",
      "hasMass": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/Gram",
        "value": 224
      },
    },
    {
      "hasVolume": {
        "type": "http://ontology.projectchronos.eu/subsystems/cubicMillimeters",
        "value": 16
      },
      "manufacturer": "Chronos",
      "type": _SERVICE + "/subsystem/Spacecraft_Structure",
      "hasMonetaryValue": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/Euro",
        "value": 18420
      },
      "minWorkingTemp": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/DegreeCelsius",
        "value": -38
      },
      "name": "70KV structure",
      "isStandard": "Cubesat",
      "maxWorkingTemp": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/DegreeCelsius",
        "value": 42.0
      },
      "uuid": "128",
      "hasMass": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/Gram",
        "value": 19.0
      },
    },
    {
      "hasVolume": {
        "type": "http://ontology.projectchronos.eu/subsystems/cubicMillimeters",
        "value": 74
      },
      "manufacturer": "Chronos",
      "type": _SERVICE + "/subsystem/Spacecraft_Communication",
      "hasMonetaryValue": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/Euro",
        "value": 4250
      },
      "minWorkingTemp": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/DegreeCelsius",
        "value": -34
      },
      "name": "65WNT communication",
      "hasPower": {
        "type": "http://dbpedia.org/data/Watt.ntriples",
        "value": -164
      },
      "isStandard": "Cubesat",
      "maxWorkingTemp": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/DegreeCelsius",
        "value": 61.0
      },
      "uuid": "129",
      "hasMass": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/Gram",
        "value": 95.0
      },
    },
    {
      "hasVolume": {
        "type": "http://ontology.projectchronos.eu/subsystems/cubicMillimeters",
        "value": 40
      },
      "manufacturer": "Chronos",
      "type": _SERVICE + "/subsystem/Spacecraft_AODCS",
      "hasMonetaryValue": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/Euro",
        "value": 12370
      },
      "minWorkingTemp": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/DegreeCelsius",
        "value": -34
      },
      "name": "29SD attitude and orbit control",
      "isStandard": "Cubesat",
      "maxWorkingTemp": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/DegreeCelsius",
        "value": 62.0
      },
      "uuid": "130",
      "hasMass": {
        "type": "http://sw.opencyc.org/2012/05/10/concept/en/Gram",
        "value": 43.0
      },
    }


  ]


subsystems = [
  {
    "name": "Spacecraft_Propulsion",
    "json+ld": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Propulsion"
  },
    {
    "name": "Spacecraft_AODCS",
    "json+ld": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS"
  },
  {
    "name": "Spacecraft_PrimaryPower",
    "json+ld": "http://ontology.projectchronos.eu/subsystems/Spacecraft_PrimaryPower"
  },
  {
    "name": "Spacecraft_BackupPower",
    "json+ld": "http://ontology.projectchronos.eu/subsystems/Spacecraft_BackupPower"
  },
  {
    "name": "Spacecraft_Thermal",
    "json+ld": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal"
  },
  {
    "name": "Spacecraft_Structure",
    "json+ld": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Structure"
  },
  {
    "name": "Spacecraft_CDH",
    "json+ld": "http://ontology.projectchronos.eu/subsystems/Spacecraft_CDH"
  },
  {
    "name": "Spacecraft_Communication",
    "json+ld": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Communication"
  }
]