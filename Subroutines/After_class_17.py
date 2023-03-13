def letter_frequency():
    count = 0
    for x in sentence:
        if x == letter:
            count = count + 1
    print(count)
letter = input("Enter the searched letter: ")
sentence = "You never get a second chance to make a first impression"

letter_frequency()