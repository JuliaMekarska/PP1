def Feet(h):
    f=h//30.48
    return f

def Inches(h):
    i=((h/30.48)-(h//30.48))*12
    return i

h=155

print(f"I am {h}cm tall, i.e. {Feet(h)} feet and {Inches(h)} inches.")