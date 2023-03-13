x=int(input("Enter the dog's age in human years: "))
y=(x*10.5)
z=(2*10.5 + (x-2) * 4)

if x<=2:
    print(f"The dog's age in dog’s years is {y} years.")

else:
    print(f"The dog's age in dog’s years is {z} years.")