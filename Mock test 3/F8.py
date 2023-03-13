import xml.etree.ElementTree as ET

class C():
    
    def __init__(self):
        
        self.root = ET.parse("mockdata.xml").getroot()
        
    def m(self, n1, n2):
        
        counter = 0
        
        for family in self.root:
            
            if int(family.find("wife").find("age").text) >= n1 and len(family.find("children").findall("name")) >= n2:
                
                counter += 1
                
        return counter
            
            