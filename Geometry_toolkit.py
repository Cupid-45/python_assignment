import math
class shapecalc:
         def area(self,a,b=None):
              if b is None:
                     return math.pi*a*a
              else:
                     return a*b

calc=shapecalc()
print("Area of circle: ",calc.area(5))
print("Area of rectangle: ",calc.area(4,6))
