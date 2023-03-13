from Contact import Contact
from Contact_list import Contact_List

john = Contact("John Brown", "brown@onet.pl", "555234000")
anna = Contact("Anna May", "am@o2.pl", "232000199")
george = Contact("George Small", "smallg@google.pl", "222999100")
paola = Contact("Paola Big", "bigpaola@poczta.pl", "100200300")

list = Contact_List()
list.add(john)
list.add(anna)
list.add(george)
list.add(paola)
list.display()

                