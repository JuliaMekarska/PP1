def Bmi(w, h):
    x=w/h**2
    return x

height=float(input("Enter your height in m:"))
weight=int(input("Enter your weight in kg:"))

print("BMI index:", Bmi(weight, height)) 