import re

file = open("grades.txt", "r")
suma = 0

for line in file:

    grades = re.findall("\d+\.\d+", line)
    
for element in grades:
    
    element = float(element)
    suma += element
    
arithmetic_mean = suma/len(grades)

print(f"Arithmetic mean: {arithmetic_mean}")
    
