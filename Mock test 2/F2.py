def f2(a1, a2):
    
    a1 = []
    a2 =[]
    count1 = 0
    count2 = 0
    
    for element1 in a1:
        
        for element2 in a2:
            
            if  0 < element2 // 10 < 10:
                
                count2 += 1
            
        if 0 < element1 // 10 < 10:
                
            count1 += 1
                
    if count1 == count2:
        
        return True
    
    else:
        
        return False
                
                
                