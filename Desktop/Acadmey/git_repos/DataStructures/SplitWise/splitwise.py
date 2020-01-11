
from abc import ABC, abstractmethod
class User:
    __new_uid = 0
    #in case of database it can be row_gen() 
    #in case of in-memory use static attribute
    name = None
    email = None
    #email can't be uid as it can change in future
    _hashedpass  = None
    
    def __init__(self, name, email, hashedpass):
        self.uid = User.__new_uid
        User.__new_uid += 1
        self.name = name
        self.email = email 
        self._hashedpass = hashedpass

    @property 
    def hashedpass(self):
        return self._hashedpass
    @hashedpass.setter 
    def hashedpass(self, hashedpass):
        
        self._hashedpass = hashedpass
        
"""
user = User("Abhishek", "abhisheksinghpnp", 123454)
user.hashedpass = "10000"
print(user.hashedpass)
"""

class Expense(ABC):
    __new_uid = 0 
    name = None
    date = None
    images = None
    notes = None 
    location = None
    _total_amount = None
    create_by: User 
    paid_by: User
    splits = [None] #type of split class
    
    """ split_amoung = {} store user and the amount the suppose to pay"""
    """in-future if we want to add notes to each split would be hard to handle this ways
    let's create class split"""
    
    """builder pattern can be used but python take care this by named Paramters"""
    def __init__(self, name,total_amount, date = None, images=None, notes = None, location = None):
        self.uid = Expense.__new_uid 
        Expense.__new_uid += 1
        self.name = name
        self.date = date
        self.images = images
        self.notes = notes 
        self.location = location 
        self._total_amount = total_amount 
    
    @property
    def total_amount(self):
        return self._total_amount
    @total_amount.setter 
    def total_amount(self, amount):
        if amount not in [1-9]:
            raise Exception("amount value is not valid")
        else:
            self._total_amount = amount 
    
    @abstractmethod 
    def validate(self,):
        pass
            
    
"""" 
exense_diwali = Expense("Abhishek", "123s12")
#exense_diwali.total_amount = "1213s2"
print(exense_diwali.total_amount)
"""

class EqualExpense(Expense):
    pass
class PartExpense(Expense):
    pass 
class PercentExpense(Expense):
    pass 
class ExactAmountExpense(Expense):
    pass

class Split(ABC):
    user: User 
    amount:float #amount- part, money , percentage

class EqualSplit(Split):
    pass
    
class PartSplit(Split):
    pass
class PercentSplit(Split):
    pass
class ExactAmountSplit(Split):
    pass


           
    

        
        