'''
Created on Nov 10, 2019

@author: abhisheksingh75
'''
from Enums import VehicleType
from abc import  ABC, abstractmethod
from parking_lot.DBObject import DBObject


class Vehicle(ABC, DBObject):
    plate_no: str 
    color: str 
    vehicle_type: VehicleType 
    uid: int
    
    def __init__(self, plate_no,color,vehicle_type, uid=None):
        self.vehicle_type = vehicle_type    
        self.plate_no = plate_no
        self.color = color
        self.uid = DBObject.get_uid(self)
    
    def __str__(self):
        return ("UID:"+str(self.uid)+
                "\nplate_no:"+self.plate_no+
                "\nvehicle_type:"+str(self.vehicle_type.value)+
                "\ncolor:"+self.color) 

        
class Truck(Vehicle):
    def __init__(self, plate_no, color):
        super().__init__(plate_no, color,VehicleType.TRUCK)
        

class Van(Vehicle):
    def __init__(self, plate_no, color):
        super().__init__(plate_no, color,VehicleType.VAN)

class Car(Vehicle):
    def __init__(self, plate_no, color):
        super().__init__(plate_no, color,VehicleType.Car)


class MoterCyle(Vehicle):
    def __init__(self, plate_no, color):
        super().__init__(plate_no, color,VehicleType.MOTERCYCLE)
        

class Electric(Vehicle):
    def __init__(self, plate_no, color):
        super().__init__(plate_no, color,VehicleType.ELECTRIC)

    
electic = Electric("1231231", "Red")
print(electic)
electic2 = Electric("1231231", "Red")
print(electic2)
truck = Truck("qscasc", "Blue")
print(truck)