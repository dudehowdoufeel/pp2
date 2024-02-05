import math
class Point():
    def __init__(self):
        self.x1=int(input())
        self.y1=int(input())
        self.x2=int(input())
        self.y2=int(input())
        self.point_coordinates={self.x1:self.y1,}
        self.show()
        self.move()
        self.dist()
    def show(self):
        print(self.point_coordinates)
    def move(self):
        self.point_coordinates={self.x2:self.y2,}
    def dist(self):
        self.distance=math.sqrt(pow((self.x2-self.x1), 2)+pow((self.y2-self.y1), 2))
        print(self.distance)
ex = Point()