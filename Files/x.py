personal_data = ["Julia Mękarska", "Uniwersytet Ekonomiczny w Krakowie", "Informatyka Stosowana"]

file = open('Personal_data.txt', 'w')

for element in personal_data:
    
    file.write(element)
    file.write("\n")

file.close()

file = file = open('Personal_data.txt', 'r')