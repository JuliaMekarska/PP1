class C():
    
    def __init__(self):
        
        import json
        
        with open("data.json", "r") as f:
            
            self.data = json.load(f)
            
    def m(self, n1, n2, n3):
        
        counter = 0
        
        for family in self.data:
            
            if (n1 <= family["husband"]["age"] <= n2) and len(family["children"]) >= n3:
                
                counter += 1
                
        return counter

            
            