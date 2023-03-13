import random

file = open("Random_numbers.txt", "w")

for count in range(1, 51):
    
    number = random.randrange(100, 1000)
    
    number = str(number)
    
    file.write(number)
    file.write("\n")
    
file.close()
    