array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]

for x in array1:
    
    t = True
        
    for y in array2:
            
        if ( x == y): t = False
            
    if t:
            
        print(x, end = " ")