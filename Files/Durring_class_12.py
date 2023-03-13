file = open('shopping.txt', 'a')

a = input("Enter the product: ")
file.write(a)
file.write('\n')

file = open('shopping.txt', 'r')
print(file.read())
