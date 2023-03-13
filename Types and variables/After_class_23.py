def Vat(a):
    v=0.23*a
    return v
    
a=15.84

print(f"Amount: {a} zl")

p=round(Vat(a), 2)

print("VAT 23%: ", p)
