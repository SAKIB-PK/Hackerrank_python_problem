class Powtwo:
    def __init__(self,max = 0):
        self.max = max
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n <=self.max:
            Power = 2 ** self.n
            self.n +=1
            return Power
        else:
            raise StopIteration
            


for number in Powtwo(4):
    print(number)



    
