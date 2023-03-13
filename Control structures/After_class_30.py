def primes():
    N = int(input("Enter the number od leading prime numbers: "))
    number = 1
    num_found = 0
    
    while num_found < N:
        number_of_dividers = 0
        
        for divider in range(1, number + 1):
            if number % divider == 0:
                number_of_dividers += 1
        
        if number_of_dividers == 2:
            print(number)
            num_found += 1
    
        number += 1
    
primes()
        
    