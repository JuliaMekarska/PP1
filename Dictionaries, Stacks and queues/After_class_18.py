stack = []

def push(value):
    stack.append(value)
    
def pop():
    
    if not empty():
        
        return stack.pop()
    
    else:
        
        return None
    
def empty():
    
    return ' '.join(str(e) for e in stack)

def read():
     
     return stack[len(stack) - 1]
    
def covert(num, reminder):
    
    reminder = num % 2
    
    if reminder == 0:
        
        num /= 2
        push(0)
        
    else:
        
        num = (num - 1)/2
        push(1)
        
    if num == 0:
        
        return
    
    covert(num, reminder)
    return

number = int(input("Enter natural number: "))
covert(number, 0)

print(f"Natural number: {number}")
print(f"Binary number: ", end = "")

for i in range(len(stack)):
    print(read(), end = "")
    pop()
    