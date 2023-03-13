import json

with open("students.json", "r") as file:
    
    students = json.load(file)
    
    for student in students:
        
        del student["age"]
        del student["gender"]
        del student["year of study"]
        del student["email"]
        
    with open("limited.json", "w") as limited:
        json.dump(students, limited)