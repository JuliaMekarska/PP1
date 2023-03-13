class ebook():
    
    def __init__(self, title, author, pages):
        
        self.is_open = False
        self.pages = pages
        self.cur_page = 1
        self.title = title
        self.author = author
        
    
    def open_book(self):
        
        self.is_open = True
        
    def close_book(self):
        
        self.is_open = False
        
    def read(self, num_pages):
        
        if (self.is_open):
            
            if (self.pages - self.cur_page) >= num_pages:
                self.cur_page += num_pages
            else:
                self.cur_page = self.pages
                print("The book is closed")
        
        else:
            print("The book is closed")
            
    def show_status(self):

        if (self.is_open):
            
            print(f"Book is open, title: {self.title}, author: {self.author}, pages: {self.pages}, current page: {self.cur_page}.")
            
        else:
            
            print("Book is closed")
            


    