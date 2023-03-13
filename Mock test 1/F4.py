def coins(price):
    sum = 0
    if price % 5 != 0:
        sum += price//5
        
        if (price%5)%2 != 0:
            sum += (price%5)//2
            
            if (price%5)%2 != 0:
                sum += (price%5)%2
    
    return sum