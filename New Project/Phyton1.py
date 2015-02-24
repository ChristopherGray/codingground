import math

def fill_tetrahedron(num):
    if type(num)==int or num%1==0:
        volume=((num)**3)/(6*(math.sqrt(2)))
        liters=volume/1000
        return liters
   
    else: print("Ne e cqlo chislo")
    
