class TV():
    
    def __init__(self):
        
        self.is_on = False
        self.channel_no = 1
        
    def turn_on(self):
        
        self.is_on = True
        
    def turn_off(self):
        
        self.is_on = False
        
    def set_channel(self, new_channel_no):
        
        self.channel_no = new_channel_no
        
    def show_status(self):
        
        if (self.is_on):
            
            print(f"TV is on, chanel {self.channel_no}")
            
        else:
            
            print("TV is off")
            
t1 = TV()
t1.show_status()
t1.turn_on()
t1.show_status()
t1.set_channel(5)
t1.show_status()
t1.turn_off()
t1.show_status()

