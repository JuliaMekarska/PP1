alphabet = {
    "a": 'Alfa',
    "b": 'Bravo',
    "c": 'Charlie',
    "d": 'Delta',
    "e": 'Echo',
    "f": 'Foxtrot',
    "g": 'Golf',
    "h": 'Hotel',
    "i": 'India',
    "j": 'Juliett',
    "k": 'Kilo',
    "l": 'Lima',
    "m": 'Mike',
    "n": ' November',
    "o": 'Oscar',
    "p": 'Papa',
    "q": 'Quebec',
    "r": 'Romeo',
    "s": 'Sierra',
    "t": 'Tango',
    "u": 'Uniform',
    "v": 'Victor',
    "w": 'Whiskey',
    "x": 'Xray',
    "y": 'Yankee',
    "z": 'Zulu'
    }

with open("ICAO.txt", 'w') as file:
    
    for key, value in alphabet.items():
        
        file.write('%s %s\n' % (key.upper(), value))
    
file.close()