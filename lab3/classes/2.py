class Shape:
    def __init__ (self):
        pass
    def area(self):
        pass
class Square(Shape):
    def __init__(self, length ):
        self.length=length
    def area(self):
        return self.length*self.length
    
if __name__=="__main__":
    