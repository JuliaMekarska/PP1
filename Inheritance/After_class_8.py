import random 

class phone():
    
    def __init__(self, brand, model, color):
        
        self.brand = brand
        self.model = model
        self.color = color
        self.barery_lv = None
        self.is_on = None
        
    def turn_on(self):
        
        self.is_on = True
        
    def turn_off(self):
        
        self.is_on = False
        
    def batery(self):
        
        self.barery_lv = round(random.uniform(0, 100), 2)
        
    def __str__(self):
        
        
        return f"Brand: {self.brand}\nModel: {self.model}\nColor: {self.color}\nBatery level {self.barery_lv}%\nTurned on: {self.is_on}\n"
    

cell = phone("Samsung", "Galaxy 10X", "black")
cell.batery()
cell.turn_on()
print(cell)
cell.turn_off()
print(cell)

        