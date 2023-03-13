array = [2, 3, 2, 5, 8, 1, 9, 8]

for x in array:
    
    t = True
        
    for y in array:
            
        if (x == y): t = False
            
    if t:
            
        print(y, end = " ")