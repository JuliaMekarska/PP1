x = 0
def numbers():
    quantity = 0
    sum = 0
    x = int(input("Enter number: "))
    quantity += 1
    sum = sum + x
    while x != 0:
        x = int(input("Enter number: "))
        quantity += 1
        sum = sum + x
        mean = sum/(quantity - 1)
      
    while x == 0:
        quantity -= 1
        print(f"RESULT: Quantity={quantity}, Sum={sum}, Mean={mean}")
        exit()
    
numbers()