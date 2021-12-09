import math

class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def norm(self):
        result = math.sqrt(self.x**2+self.y**2)
        return result
