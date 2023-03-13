file = open('countries.txt', 'r')
file_content = file.read()    #wskaźnik do pliku, w funkcji read jest return
print( file_content )
file.close()