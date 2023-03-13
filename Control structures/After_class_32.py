import random

def lottery():
    for i in range (1, 8):
        for j in range (1, 8):
            x = random.randint(1, 50)
            if x < 10:
                print(x, end = '  ')
            else:
                print(x, end = ' ')
        print()

lottery()