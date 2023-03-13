def Hcirc(a, b, c):
    s=(a+b+c)/2
    return s

def Area(s, a, b, c):
    x=(s*(s-a)*(s-b)*(s-c))**(1/2)
    return x

a=int(input("Enter length a:"))
b=int(input("Enter length b:"))
c=int(input("Enter length c:"))

print("Area: ", Area(Hcirc(a, b, c), a, b, c))
