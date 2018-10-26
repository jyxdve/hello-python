print(bin(4))
print(hex(10))     
print(max([1,2,3,4,5]))
print(sum([1,2,3,4,5]))
print(sorted([1,4,3,5,2]))

def square(x):
    return x * x

for y in range(5):
    print("{}**2 == {}"
       .format(y, square(y)))

#import math
#def area_circle(radius):
    #return math.pi * radius ** 2 
import geometry
data = input ("Enter your radius of " + " a circle: ")
radius = float(data)
 print("Area of the circle {:.4f}"
      .format(geometry.area_circle(radius)))