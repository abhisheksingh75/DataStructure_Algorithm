'''
Created on Nov 10, 2019

@author: abhisheksingh75
'''
from enum import Enum

class VehicleType(Enum):
    CAR = "CAR"
    TRUCK = "TRUCK" 
    VAN = "VAN"
    MOTERCYCLE = "MOTERCYCLE"
    ELECTRIC = "ELECTRIC"
    
class GateType(Enum):
    ENTRANCE = "ENTRANCE"
    EXIST = "EXIST"
    INACTIVE  = "INACTIVE"