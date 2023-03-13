import random

class thermometer():
    
    def __init___(self):
        
        self.is_on = False
        self.temp = 0
    
    def turn_on(self):
        
        self.is_on = True
        
    def turn_off(self):
        
        self.is_on = False
    
    def measure(self):
        
        if (self.is_on):
        
            self.temp = random.uniform(34.0, 42.0)
            
        else:
            
            quit
        
    def display(self):
        
        if 37 <= self.temp < 41:
            
            print(f"Temperature: {self.temp} (fever)")
            
        elif 41 <= self.temp:
            
            print (f"Temperature: {self.temp} 'CRITICAL TEMPERATURE!")
            
        else:
            
            print(f"Temperature: {self.temp}")
