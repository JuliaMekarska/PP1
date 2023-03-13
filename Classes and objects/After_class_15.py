class TV():
    
    def __init__(self):
        
        self.is_on = False
        self.channel_no = 1
        self.vol = 0
        
    def turn_on(self):
        
        self.is_on = True
        
    def turn_off(self):
        
        self.is_on = False
        
    def set_channel(self, new_channel_no):
        
        self.channel_no = new_channel_no
        
    def vol_inc(self, vol_ad):
        
        vol_ad = 1
        
        if 0 <= self.vol <= 10:
             self.vol += vol_ad
        else:
            self.vol = self.vol
            
    def vol_dec(self, vol_sub):
        
        vol_sub = 1
        
        if 0 <= self.vol <= 10:
             self.vol -= vol_sub
        else:
            self.vol = self.vol
            
        
    def show_status(self):
        
        if (self.is_on):
            
            print(f"TV is on, chanel {self.channel_no}, volume level: {self.vol}")
            
        else:
            
            print("TV is off")
            
t1 = TV()
t1.show_status()
t1.turn_on()
t1.show_status()
t1.vol_inc(1)
t1.show_status()
t1.vol_inc(1)
t1.show_status()
t1.vol_inc(5)
t1.show_status()
t1.vol_dec(3)
t1.show_status()