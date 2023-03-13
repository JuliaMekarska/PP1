class C():
    
    def __init__(self, phones):
        
        self.phones = phones
        
    def m(self):
        
        counter = 0
        
        for number_1 in self.phones:
            
            for number_2 in self.phones:
                
                if number_1 == number_2:
                    
                    counter += 1
                    
            if counter > 1:
                
                return True
            
        return False
        
print(C(["1111222333", "1234123412", "6342112326"]).m())
            
            