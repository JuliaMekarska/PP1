class C():
    
    def __init__(self, text):
        
        self.text = text
        
    def m(self):
        
        counterChars = {}
        counter = 0
        
        for char in self.text:
            
            if char not in counterChars.keys():
                
                counter = 1
                
            else:
                
                counter += 1
                
        return counterChars

                
                