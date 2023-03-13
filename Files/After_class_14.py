file = open("sample1.txt", "r")

with open("sample1.txt", "r") as file:
    contents = file.readlines()
    
    print(contents)
