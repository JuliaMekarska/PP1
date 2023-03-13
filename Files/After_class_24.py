import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C"
temperatures = re.findall("\d{2}", message)
suma = 0

for value in temperatures:
    
    value = int(value)
    suma += value
    
avarage_temperature = suma / len(temperatures)

print(f"Temperatures: {temperatures}")
print(f"Avarange temperature: {avarage_temperature}")
    
