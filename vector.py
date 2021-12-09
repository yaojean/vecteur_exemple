import math

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def norm(self):
        result = math.sqrt(self.x**2+self.y**2)
        return result
    def parite(self):
        est_paire=False
        if norm() % 2==0:
            est_paire=True

v1=Vector(4,-6)
print(v1.norm())
print(v1.parite())
