class Enrollment:
    count = 0
    def __init__(self,n,c):
        self.name = n
        self.course = c
        Enrollment.count +=1
    def display(self):
        print(self.name)
        print(self.course)