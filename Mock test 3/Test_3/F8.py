class C():
    
    def __init__(self):
        
        import xml.etree.ElementTree as ET
        
        with open("data.xml", "r") as f:
            
            self.root = ET.parse(f).getroot()
            
    def m(self, n1, n2, n3):
        
        counter = 0
        
        for family in self.root:
            
            if (int(family.find("husband").find("age") in range(n1, n2 + 1)) and len(family.find("children")("names").findall) >= n3):
                
                counter += 1
                
        return counter
