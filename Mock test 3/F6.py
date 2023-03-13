class C():
    
    def __init__(self, boolean):
        
        self.bol = boolean
        
    def m(self):
        
        counter = 0
        
        for i in range(1, len(self.bol) - 1):
                
            if self.bol[i] != self.bol[i - 1]:
                
                if self.bol[i] != self.bol[i + 1]:
                    
                    counter += 1
                    
        return counter
        
c = C([True,False,True,False])
c.m()
        
        