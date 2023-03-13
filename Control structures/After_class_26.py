PIN = input("Create a pin code: ")

for attempts in range (0,4):
    attempts = attempts + 1
    if attempts<3:
        x = (input("Enter the PIN code: "))
        print(x)
        if x != PIN:
            print("Incorrect...")
        elif x == PIN:
            print("Correct")
            exit()
            
    if attempts == 3:
        y = (input("Enter the PIN code: "))
        print(y)
        if y == PIN:
            print("Correct")
        
        elif y != PIN:
            print("Incorrect...")
            print("Sorry, your payment card has been blocked.")