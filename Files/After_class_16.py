file = open("sample2.txt", "r")

count = 0

for line in file:
    
    count += 1
    
    if count % 6 != 0:
        
        print(line)
        
    else:
        
        input("Press enter to continue")
        
file.close()
        