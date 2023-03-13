def f7(n):
    
    Fibo = {}
    Fibo[0] = 0
    Fibo[1] = 1
    
    for i in range(2, n):
        Fibo[i] = Fibo[i - 1] + Fibo[i - 2]
        
    return Fibo[n - 1]