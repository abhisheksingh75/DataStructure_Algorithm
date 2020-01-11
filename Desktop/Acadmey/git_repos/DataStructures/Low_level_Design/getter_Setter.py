
class Geeks: 
     def __init__(self): 
          self._age = 0
       
     # function to get value of _age 
     def get_age(self): 
         print("getter method called") 
         return self._age 
       
     # function to set value of _age 
     def set_age(self, a): 
        if a == 10:
            print("a:10")
        else:
            print("setter method called") 
        self._age = a 
  
     # function to delete _age attribute 
     def del_age(self): 
         del self._age 
     
     age = property(get_age, set_age, del_age)  
  
mark = Geeks() 
  
mark.age = 10