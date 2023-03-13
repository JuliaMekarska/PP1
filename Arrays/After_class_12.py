array1 = [15, 8, 31, 47, 2, 19]
array2 = []

def change(array1, array2):

    for element in range(len(array1) - 1, -1, -1):
        
        array2.insert(0, array1[element])
        
    print("Existed array: ", array1)
    print("Reverse array: ", array2)
    
    return array2

print(change(array1, array2))