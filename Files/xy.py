my_file = open("test_file.txt", "w")
my_file.write("abc\n")
my_file.write("123")
my_file = open("test_file.txt")
content = my_file.read()
my_file.close()