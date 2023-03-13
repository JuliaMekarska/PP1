file = open("Powers.txt", "w")

for number in range (1, 11):
    
    second_power = number ** 2
    third_power = number ** 3
    
    number = str(number)
    second_power = str(second_power)
    third_power = str(third_power)
    
    file.write(number)
    file.write(",")
    file.write(second_power)
    file.write(",")
    file.write(third_power)
    file.write("\n")
    
file.close()