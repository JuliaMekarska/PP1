def f5(n):
    n = str(n)
    count = 0
    for digit in n:
        if (int(digit)) % 2 == 0:
            count += 1
    return count