#!/usr/bin/python3

class Square():
    
    def __init__(self, width):
        self.width = width

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        return self.width * 4

    def __str__(self):
        return "{} by {} by {} by {}".format(self.width, self.width, self.width, self.width)

if __name__ == "__main__":

    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
