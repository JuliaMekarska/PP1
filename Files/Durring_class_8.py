file = open('countries.txt', 'r')

count = 0

for line in file:
    
    count += 1
    print(count, ". ", line, sep = '', end = "")

file.close()