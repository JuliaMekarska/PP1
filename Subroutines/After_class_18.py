def sum(number):
    number = str(number)
    sum_of_digits = 0
    for digit in number:
        sum_of_digits += int(digit)
    
    return sum_of_digits
