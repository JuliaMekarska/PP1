array = list(input("Enter the array: "))

def bubblesort(array):
    
    for i in range(0, len(array) - 1):
        
        for j in range(len(array) - 1):
            
            if (array[j] > array [j + 1]):
                
                x = array[j]
                array[j] = array[j + 1]
                array[j + 1] = x
    
    return array

print("The unsorted list is: ", array)
print("The sorted list is: ", bubblesort(array))