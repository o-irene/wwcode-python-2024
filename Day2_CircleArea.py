# Task: Create a program to calculate the area of a circle given its radius.
import math


def calc_circle_area(radius):
    pi_number = math.pi
    area = radius ** 2 * pi_number
    return area


user_radius = input("To find the circle area, print the radius: ")

try:
    circle_area = calc_circle_area(float(user_radius))
    print(f"The area of your circle is {circle_area}.")
except ValueError:
    print("Oops! To calculate the circle area, please, input only numbers.")
