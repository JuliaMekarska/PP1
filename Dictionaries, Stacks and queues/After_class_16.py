word = input('Enter word: ')

def otan(word):
    
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
    
    phon = [alphabet[w] for w in word]
    
    x = ' '.join(phon)
    y = f"Spelled text: {x}"
    
    return y

print(otan(word))
