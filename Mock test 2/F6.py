import csv

def f6(g, n1, n2):
    
    count = 0
    
    with open("people.csv") as file:
        
        people = csv.DictReader(file)
        
    for human in people:
        
        if human['gender'] == g and int(human['height']) in range(n1, n2 + 1):
            
            count += 1
    
    return count
    
            