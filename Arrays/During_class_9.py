def month(x):
    
    months = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj',
              'Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień',
              'Październik', 'Listopad', 'Grudzień']
    
    return months[x - 1]

print(month(5))