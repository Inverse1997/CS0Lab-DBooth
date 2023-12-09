"""
Lab - Object Oriented Programming (OOP)
By: Daniel Booth

CSCI 110
Date: 12/08/2023

Object Oriented Programming:
Using user-defined class/type, program finds area and 
circumference of a circle.
"""

import math

class Circle(object):
    """
    Class that represents a circle with three attributes – radius, area and circumference.
    Class has two user-defined methods findArea and findCircumference and two special 
    built-in methods:   __init__ and __str__.
    """

    def __init__(self, r=0):
        self.radius = r
        self.area = self.findArea()
        self.circumference = self.findCircumference()

    def findArea(self):
        return math.pi * (self.radius ** 2)

    def findCircumference(self):
        # FIXED: Find and return the circumference of the circle (20 pts)
        return 2 * math.pi * self.radius  

    def __str__(self):
        # FIXED: Modify the statement to return circumference as well (20 pts)
        return "Circle - radius: {:.2f}, area: {:.2f}, and circumference: {:.2f}".format(
            self.radius, self.area, self.circumference)  

def main():
    # instantiate aCir object with radius 1
    aCir = Circle(1)
    print(aCir)

    # FIXED: (20 pts)
    # Instantiate another circle with radius 5
    # Print the circle
    anotherCir = Circle(5) 
    print(anotherCir)  

    # FIXED: (20 pts)
    # prompt user to enter radius and store into a variable
    user_radius = float(input("Enter the radius: ")) 

    # FIXED (20 pts)
    # create a circle with the user provided radius
    # print the circle
    userCir = Circle(user_radius) 
    print(userCir) 

if __name__ == "__main__":
    main()
