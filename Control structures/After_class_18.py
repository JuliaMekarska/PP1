x=int(input("Enter the natural amount in PLN: "))
a=x//5
b=(x%5)//2
c=((x%5)%2)

if x%5==0:
    print(f"The amount of PLN {x} in coins: ")
    print(f"5zł - {a}")

elif x%5!=0 and (x%5)%2==0:
    print(f"The amount of PLN {x} in coins: ")
    print(f"5zł - {a}")
    print(f"2zł - {b}")
    
elif x%5!=0 and (x%5)%2!=0:
    print(f"The amount of PLN {x} in coins: ")
    print(f"5zł - {a}")
    print(f"2zł - {b}")
    print(f"1zł - {c}")