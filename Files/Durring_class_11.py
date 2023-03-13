films = ["Inception", "Titanic", "John Wick", "Diuna", "Ring"]

x = open("Films.txt", "w")

for film in films:
    
    x.write(film)
    x.write("\n")
    
x.close()