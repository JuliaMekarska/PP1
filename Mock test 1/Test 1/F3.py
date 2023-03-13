def f3(x, y):
    count = 0
    for i in range (x, y + 1):
        if i % 2 == 0 and i < 0:
            count += 1
    
    return count
        