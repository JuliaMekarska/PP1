import re

def f5(c):
    
    with open("poem.txt") as file:
        
        count = 0
        
        for line in file:
            
            matches = re.findall(c, line)
            
            if len(matches) > 0:
                
                count += 1
                
    return count
            