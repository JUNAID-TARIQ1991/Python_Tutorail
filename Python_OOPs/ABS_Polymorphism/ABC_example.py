from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def sides(self):
        pass


class Square(Polygon):
    def sides(self):
        print("I have four sides")


class Pentagon(Polygon):
    def sides(self):
        print("I have five sides")


square1 = Square()
square1.sides()
