from abc import ABC, abstractmethod
from parking_lot import DBObject

from Enums import GateType

from abc import ABC, abstractclassmethod
class Gate(ABC, DBObject):
    gate_no: int
    gate_type: GateType
    
    def __init__(self, gate_no, uid=None):
        self.gate_no = gate_no
        self.uid = DBObject.get_uid(self)
    
    def open(self): 
        pass
    
    def close(self):
        pass

class ExistGate(Gate):
    
    def __init__(self, gate_no):
        super().__init__(gate_no)
    def __str__(self):
        return ("gate_uid:"+str(self.uid)+
                "\ngate_no:"+str(self.gate_no))
    
