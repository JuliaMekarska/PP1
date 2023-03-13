import random

def read_number():
    number = int(input("Enter the number: "))
    return number

def generate_number():
    number = random.randint(1, 9)
    return number