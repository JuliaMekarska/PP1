class C():
    
    def __init__(self, text):
        
        self.text = text
        
    def m1(self):
        
        counterChars = {}
        
        for letter in self.text:
            
            if letter in counterChars.keys():
                
                counterChars[letter] += 1
                
            else:
                
                counterChars[letter] = 1
                
        return counterChars
        
    def m2(self, c1):
        
        countedChars = self.m1()
        countedPassedChars = {}
        
        for letter in c1:
            
            countedPassedChars[letter] = countedChars[letter]
            
        return countedPassedChars
    
print(C("my moon").m1())
print(C("my moon").m2("mn"))
      
        