class C():
    
    def __init__(self, number):
        
        self.number = number
        
    def __str__(self):
        
        if self.number < 0:
            
            return ""
        
        else:
            
            return self.number * "*"
        
