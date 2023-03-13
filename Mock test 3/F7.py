import json

class C():
    
    def __init__(self):
        
        with open ("mockdata.json") as mockdata:
            
            self.families = json.load(mockdata)
        
    def m(self, n1, n2):
            
        counter = 0
        
        for family in self.families:
        
            if int(family["wife"]["age"]) >= n1 and len(family["children"]) >= n2:
                
                counter += 1
                
        return counter
        
    def m2(self, n1):
        
        families = []
        
        for family in self.families:
            
            if len(family["children"]) >= n1:
                
                families.append(family)
                
        with open ("mockdata1.json", "w") as mockdata1:
            
            json.dump(families, mockdata1, indent = 2)     
                
print(C().m(21, 2))
C().m2(2)
 
        
        