class Box:
    def __init__(self, size):
        self.size = size
    
    def double(self):
        self.size = self.size * 2

x = Box(5)
y = x
y.double()
x.double()

print(x.size, y.size)