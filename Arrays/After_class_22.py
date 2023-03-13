array_str = list(input("Enter the array: "))
array_ints = []

def difference(array_str):

    for x in array_str:
        
        array_ints.append(int(x))
    
    for i in array_str:
        
        x = max(array_ints)
        y = min(array_ints)
        z = x - y
    
        return z 

print(difference(array_str))