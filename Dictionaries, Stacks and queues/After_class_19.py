import During_class_10

stack = []

while True:
    
    x = input("Enter sign: ")
    
    if x == "+":
        y = stack.pop()
        w = stack.pop()
        z = y + w
        stack.append(z)
        
    elif x == "*":
        y = stack.pop()
        w = stack.pop()
        z = y * w
        stack.append(z)
        
    elif x == "/":
        y = stack.pop()
        w = stack.pop()
        z = y / w
        stack.append(z)
        
    elif x == "=":
        y = stack.pop()
        stack.append(y)
        print(y)
        
    else:
        stack.append(int(x))
        