class C():
    
    def __init__(self, array):
        
        self.array = array
        
    def m(self):
        
        for i in range(len(self.array) - 1):
            
            if (int(self.array[i]) % 2 == 0 and i % 2 != 0) or (int(self.array[i]) % 2 != 0 and i % 2 == 0):
                
                return False
            
        return True

                
