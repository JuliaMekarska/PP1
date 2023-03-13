file_name = str(input("Enter the file's name: "))

count = 0

file = open(f"{file_name}", "r")

for line in file:
    
    count +=1
    
file.close()

print(f"File name: {file_name}")
print(f"Number of lines: {count}")