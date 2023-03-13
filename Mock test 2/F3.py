import re

def f3(t):
    
    numbers = re.findall("\d+", t)
    
    suma = 0
    
    for i in numbers:
        
        num = int(i)
        
        if 9 < num < 1000:
            
            suma += num
            
    return suma
