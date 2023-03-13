numbers = [-15, 8, - 31, 47, -2, 19]

maximum = 0
minimum = 0

for i in range (1, len(numbers)):
        
        if numbers[i] > maximum: maximum = numbers[i]
        
        if numbers[i] < minimum: minimum = numbers[i]
    
print(maximum)
print(minimum)

