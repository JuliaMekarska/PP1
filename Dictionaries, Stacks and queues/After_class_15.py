import json

student_data = {
    "surname": 'Kowalsky',
    "name": 'Andrzej',
    "age": 20,
    "adress": 'Karmelicka 35, 30-082 Krakow',
    "phone_numbers": { "work": 511423654, "private": 927183756},
    }

with open("student.json", "w") as file:
    
    json.dump(student_data, file, indent = 4)
    
file.close()