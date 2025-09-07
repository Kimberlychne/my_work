from shapes import Rectangle, Circle, Triangle
import utils

def welcome_message():
    print("welcome to shape Toolkit!")
    print("we support Rectangles, Circles, and Triangles")

def main():
    welcome_message()

    shapes = [
        Rectangle(5,10),
        Circle(7),
        Triangle(6,4)
    ]
    #adding shapes to lists so i can loop through and execute some action for each shape
    for shape in shapes:
        shape.describe()
        are_cm2 = shape.area()


main()