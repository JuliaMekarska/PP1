class C():
    
    def __init__(self, name, surname):
        
        self.name = name
        self.surname = surname
        
    def __str__(self):
        
        return f"{self.name[0].upper()}{self.surname[0].upper()}"
    

c = C("anna","may")
print(c)