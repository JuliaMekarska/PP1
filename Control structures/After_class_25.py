a=int(input("Enter a dimension: "))
b=int(input("Enter b dimension: "))
x=("*")

print(b*"*")

for i in range(a-2):
    print("*" + (b-2)*' ' + "*")

print(b*"*")
    