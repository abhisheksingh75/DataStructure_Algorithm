from abc import ABC,abstractmethod 

class polygon(ABC):
    @abstractmethod
    def no_of_sides(self):
        pass
    def ispolygon(self):
        print("yes")
        

class Triange(polygon):
    
    def triange_len(self):
        print("triange_len")
    def no_of_sides(self):
        print("three")


o_obj = Triange()
o_obj.triange_len()
o_obj.ispolygon()
pol = polygon()