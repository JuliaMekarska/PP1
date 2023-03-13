numbers = [15, 8, 31, 47, 2, 19]

suma = 0

for digit in range(len(numbers)):
    
    suma += numbers[digit]
    
mean = suma/len(numbers)

print(mean)