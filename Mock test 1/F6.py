import random

def rand(fro, to):
    x = random.randint(fro, to)

    for x in range(fro, to):
        if x % 2 == 0 and x % 3 == 0:
            
            return x