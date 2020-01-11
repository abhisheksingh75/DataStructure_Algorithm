class Singleton:
   instance = None
   @staticmethod 
   def getInstance():
      """ Static access method. """
      if Singleton.instance == None:
        Singleton()
      return Singleton.instance
   def __init__(self): 
    if self.instance == None:
        #network connection
        #db connection 
        #query
        #prase
        #return query
        Singleton.instance = self
    else:  
      """ Virtually private constructor. """
      raise Exception("This class is a singleton!")

h = Singleton()
print(h)
l = Singleton()
print(l)
s = Singleton.getInstance()
print(s)
j = Singleton.getInstance()
print(j)


