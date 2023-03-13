def compare(array1, array2):
    
    print("Array1: ", array1)
    print("Array2: ", array2)
    
    if len(array1) != len(array2):
        
        print("Comparison: arrays are not the same")
        return False
    
    else:
        
        for element in range(0, len(array1) + 1):
            
            if array1[element] != array2[element]:
                
                print("Comparison: arrays are not the same")
                return False
            
            else:
                
                print("Comparison: arrays are the same")
                return True

print(compare(["water","book","sky"], ["water","book","sky"]))
print(compare([True,False], [True,False,True]))
print(compare([5,3,1], [5,3,1]))
print(compare([3,2,1], [3,2]))
            


            

    