class C():
    
    def __init__(self, dic):
        
        self.dic = dic
        self.value = 0
        self.place_1 = len(self.dic["value"]) - 1
        self.place_2 = len(self.dic["value"]) - 1
        
    def m(self):
        
        if self.dic["system"] == "2":
            
            for digit_1 in self.dic["value"]:
                
                digit_1 = int(digit_1)
                
                if digit_1 >= 2:
                    
                    return -1
                
                else:
                    
                    self.value += digit_1 * (2 ** self.place_1)
                    
                    self.place_1 -= 1
                    
            return self.value
            
            
        elif self.dic["system"] == "8":
            
            for digit_2 in self.dic["value"]:
                
                digit_2 = int(digit_2)
                
                if digit_2 >= 8:
                    
                    return -1
                
                else:
                    
                    self.value += digit_2 * (8 ** self.place_2)
                    
                    self.place_2 -= 1
                    
            return self.value
        
c = C({"system":"8", "value":"70271"})
c.m()
        
        
                    
        
        