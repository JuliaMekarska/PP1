class Statics():
    
    def __init__(self, array):
        
        self.array = array
        self.suma = None
        self.maximum = None
        self.minimum = None
        self.mean = None
        self.median = None
    
    def add(self):
        
        self.array.append(int(input("Enter the next number: ")))

    def display_row(self):
        
        print(", ".join(map(str, self.array)))
            
    def the_greatest(self):
        
        self.maximum = max(self.array)
        
    def the_smallest(self):
        
        self.minimum = min(self.array)
        
    def a_mean(self):
            
        self.mean = sum(self.array)/len(self.array)
        
    def med(self):
        
        sorted_array = sorted(self.array)
        
        if len(self.array) % 2 == 0:
            
            self.median = (sorted_array[len(sorted_array) // 2] + sorted_array[len(sorted_array) // 2 + 1]) / 2
            
        else:
            
            self.median = sorted_array[len(sorted_array) // 2]
        
    def display(self):
        
        print(f"The greatest number is: {self.maximum}")
        print(f"The smallest number is: {self.minimum}")
        print(f"The mean is {self.mean}")
        print(f"The median is {self.median}")
        
stat = Statics([12, 37, 6, 9, 17])
stat.add()
stat.display_row()
stat.the_greatest()
stat.the_smallest()
stat.a_mean()
stat.med()
stat.display()
            