file = open('numbers.txt', 'r')
suma = 0

for line in file:
    
    suma += int(line)

file.close()

print(suma)