class Contact_List():
    
    def __init__(self):
        
        self.array = []
    
    def add(self, contact):
        
        self.array.append(contact)
    
    def display(self):
        
        for contact in self.array:
            
            print(f"{contact.name} {contact.email} {contact.telephone}")