file = open("Numbers.txt", "w")

for number in range(1, 51):
    number = str(number)
    file.write(number)
    file.write("\n")

file.close()