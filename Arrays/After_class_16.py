array = [12, 6, 4, 9, 10]

def star(n):
    x = ''
    
    for i in array:
        x = n * "*"
        
    return x
        
for i in range(len(array)):
    lenght = array[i]
    print(f"{lenght}: ", star(lenght))
    