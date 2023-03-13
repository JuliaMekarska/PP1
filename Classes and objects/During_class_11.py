class TV():
    
    def __init__(self, channel_no):
        
        self.is_on = False
        self.channel_no = 1
        
    def turn_on(self):
        
        self.is_on = True
        
    def turn_off(self):
        
        self.is_on = False
        
    def show_status(self):
        
        if (self.is_on):
            
            print(f"TV is on, chanel {channel_no}")
            
        else:
            
            print("TV is off")