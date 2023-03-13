class C():
    
    def __init__(self, sentence):
        
        self.sen = sentence
        
    def m(self):
        
        for i in self.sen:
            
            counter = 0
            
            for j in self.sen:
                
                if i == j:
                    
                    counter += 1
                    
            if counter > 1:
                        
                return False
                    
        else:
                        
            return True
                    
                
print(C("red sun").m())
print(C("blue water").m())
print(C("BLUE water").m())
