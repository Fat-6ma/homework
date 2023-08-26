#8/8/2023
import math  
pi = math.pi

ra=input("value of radius: ")
he=input("value of height: ")
  
def find_Volume_of_cone(r,h):  
    return (pi *  r * r * h ) / 3 
  
radius = print(ra)  
height = print(he)
print(find_Volume_of_cone(radius, height))  