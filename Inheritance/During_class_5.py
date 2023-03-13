class music():
    
    def __init__(self, artist, track_title, album, year):
        
        self.artist = artist
        self.title = track_title
        self.album = album
        self.year = year
        
    def __str__(self):
        
        return "Performer: " + self.artist + "\n" + "Song: " + self.title + "\n" + "Album: " + self.album + "\n" + "Year: " + self.year + "\n"
    
        
E_S = music("Ed SHeeran", "Hearts Don't Break Around Here", "Divide", "2017")
print(E_S)

D_B = music("David Bowie", "Let's dance", "Let's dance", "1983")
print(D_B)

M_M = music("Of monsters and men", "Little talks", "My head is an animal", "2011")
print(M_M)
