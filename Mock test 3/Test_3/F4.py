class C():
    
    def __init__(self, array):
        
        self.array = array
        
    def m(self):
        
        change = self.array[1] - self.array[0]
        
        for i in range(len(self.array) - 1):
            
            if self.array[i + 1] - self.array[i] != change:
                
                return - 1
                
        return change