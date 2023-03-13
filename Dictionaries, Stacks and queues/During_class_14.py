import json

fav_film = {
    
    "Title": "Inception",
    "Director": "Christopher Nolan",
    "Date": 2010,
    "Language": "english",
    "Rating": 9
    }

with open("favourite.json", "w") as file:
    
    json.dump(fav_film, file, indent = 4)
