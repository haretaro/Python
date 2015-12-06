class Iterator:

    def __init__(self):
        self.i = 0

    def __next__(self):
        if self.i > 5:
            raise StopIteration()
        self.i += 1
        return self.i

    def __iter__(self):
        return self

iterator = Iterator()
for x in iterator:
    print(x)

    
