class University():

    def __init__(self, name):
        self.name = name    

    def print_name(self):  
        print(self.name)
        
    def set_name(self, name):
        self.name = name

u1 = University("UEK")
u1.print_name()
u1.set_name("AGH")
u1.print_name()
