array1 = list(input("Enter the array: "))

def powers(array1):
    
    array2 = []
    
    for element in array1:
        
        element = int(element)
        element = element**2
        array2 = element
        
    return array2
    
    print("Array: ", array1)
    print("2nd power: ", array2)

print(powers(array1))