class C():
    
    def __init__(self, ip):
        
        self.ip = ip
        
    def m(self):
        
        self.ip = self.ip.split(".")
        
        if len(self.ip) != 4:
            
            return False
        
        for ip_part in self.ip:
            
            if int(ip_part) < 0 or int(ip_part) > 255:
                
                return False
            
        else:
                
            return True