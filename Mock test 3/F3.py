class C():
    
    def __init__(self, names):
        
        self.names = names
        self.count = 0
        
    def m(self):
        
        for name_1 in self.names:
            
            for name_2 in self.names:
                
                if name_1.lower() == name_2.lower():
                    
                    self.count += 1
                
            if self.count > 1:
                
                return True
            
            else:
                
                return False 
        
c = C(["ANNA","John","Anna"])
c.m()