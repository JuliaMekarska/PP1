class University():

    def __init__(self, name, fullname):
        self.name = name
        self.fullname = fullname

    def print_name(self):  
        print(self.name)
        
    def set_name(self, name):
        self.name = name
    
    def print_fullname(self):
        print(self.fullname)
        
    def set_fullname(self, fullname):
        self.fullname = fullname
        
u1 = University("Uek", 'Uniwersytet Ekonomiczny w Krakowie')
u1.print_name()
u1.print_fullname()
u1.set_name("UJ")
u1.set_fullname("Universytet Jagielloński")
u1.print_name()
u1.print_fullname()


        
