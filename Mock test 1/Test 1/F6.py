def f6(x, n):
    wyraz = 1
    i = 1
    
    while i != n:
        if (wyraz + x) % 2 != 0:
            i += 1
        wyraz += x
    return wyraz