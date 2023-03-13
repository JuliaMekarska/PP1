from Ebook import ebook

ebook = ebook("Moby Dick", "Herman Melville", 378)
ebook.open_book()
ebook.show_status()
ebook.read(36)
ebook.show_status()
ebook.close_book()
ebook.show_status()