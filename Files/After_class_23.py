import csv

with open("students.txt") as file:
    
    content = csv.reader(file, delimiter = ",")
    next(content)
    
    for i in content:
        if int(i[2]) < 30:
            
            print(i[0], i[1], i[4])
