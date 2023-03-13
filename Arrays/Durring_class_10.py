array = [-15, 8, - 31, 47, -2, 19]

def sum(array):
    
    sum = 0
    
    for digit in array:
        sum += digit
    
    return sum

print(sum(array))

def array2str(array):
    
    together = " "
    for digit in array:
        together += str(digit)
        together += " "
    
    return together

print(array2str(array))
    
    
