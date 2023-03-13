i = 0
def Fibonacci(i):
    a = 0
    b = 1
    for i in range(0, 50):
        if i == 0:
            print(a)
        elif i == 1:
            print(b)
        else:
            c = a + b
            a = b
            b = c
            print(c)
    
Fibonacci(i)