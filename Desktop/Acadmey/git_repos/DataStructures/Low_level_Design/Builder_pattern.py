class Bird:
    height, weight, col = None, None, None
    def __init__(self, builder):
        self.height = builder.height
        self.weight = builder.weight
        self.col = builder.col



class Builder:
    height, weight, col = None, None, None
    
    def setheight(self, height):
        self.height = height
        return self
    def setweight(self, weight):
        self.weight = weight
        return self
    def setcol(self, col):
        self.col = col
        return self
    def build(self):
        O_Bird = Bird(self)
        return O_Bird


o_bird = Builder().setheight(10).setweight(20).build()
print(o_bird.height)

birdlist = [Bird(Builder())]*5

b = Bird(Builder())

###################333
#Named parameters 
class Bird2:
    height, weight, col = None, None, None
    def __init__(self, height=None,weight=None,col=None):
        self.height = height
        self.weight = weight
        self.col  = col
        
o_bject = Bird2(height = 20, col= 'green')
print(o_bject.height)
print(o_bject.col)
            
        
        

