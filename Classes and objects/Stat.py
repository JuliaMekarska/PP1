class Statics():
    
    def __init__(self, array):
        
        self.array = array
    
    def add(self):
        
        self.array[5] = print(int(input("Enter the next number")))
        
    def display(self):
        
        for i in self.array:
            
            print(i)
            
    def the_greatest(self):
        
        maximum = max(self.array)
        
    def the_smallest(self):
        
        minimum = min(self.array)
        
    def mean(self):
        
        for i in self.array:
            
            suma += i
            
        mean = suma/len(array)
        
    def median(self):
        
        n = len(array)
        
        for i in range(n - 1):
            
            if array[j] > array[j + 1]:
                
                array [j], array[j + 1] = array[j + 1], array[j]
                
        if n%2 == 0:
            
            median = (n/2 + (n/2 + 1))/2
            
        else:
            
            median = (n + 1)/2
        
    def display(self):
        
        print(f"The greatest number is: {maximum}")
        print(f"The smallest number is: {minimum}")
        print(f"The mean is {median}")
        print(f"The median is {median}")
        
        
            