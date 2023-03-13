number = int(input("Enter the number: "))
array_str = list(input("Enter the array: "))
array_ints = []

def occurs(number, array_str):
    
    for x in array_str:
        
        array_ints.append(int(x))
        
    for element in array_ints:
    
        while element != number:
            
            element += array_ints[]
        
        if element == number:
        
            print("Number: ", number)
            print("Array: ", array_ints)
            print(f"Result: number {number} appears in the array")
        
            return True
        
            
            print("Number: ", number)
            print("Array: ", array_ints)
            print(f"Result: number {number} doesn't appear in the array")
            
            return False
        
print(occurs(number, array_str))


    