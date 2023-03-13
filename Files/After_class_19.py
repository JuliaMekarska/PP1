file1 = open("shoppinglist.txt", "w")
file2 = open("GrainsAndBread.txt", "r")
file3 = open("MeatAndFish.txt", "r")

for line in file2:
    
    file1.write(line)
    
for line in file3:
    
    file1.write(line)
    
file1.close()
file2.close()
file3.close()