stack = []

def push(value):
    stack.append(value)
   
def pop():
    if not empty():
        return stack.pop()
    else:
        return None

def empty():
    return len(stack) == 0

def display():
    for i in stack:
        print(i, end=" ")
    print()
