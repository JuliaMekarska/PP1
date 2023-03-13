class C:
    def __init__(self, numbers):
        self.numbers = numbers
        
    def m(self):
        for i in range(len(self.numbers)):
            if (i%2 == 0 and self.numbers[i] % 2 != 0) or (i%2 != 0 and self.numbers[i] % 2 == 0):
                return False
        return True
    
print(C(["1", "2", "3", "4", "5", "6"]).m())