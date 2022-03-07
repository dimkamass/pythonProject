"""
Input: radius
Output: lenght of circle
"""

from math import pi


def circle_area(radius):
    if radius < 0:
        raise ValueError('radius cant be negative')
    elif type(radius) not in (int, float):
        raise TypeError('Type must be int or float')
    else:
        return pi * radius ** 2


print('Input radius:', end=' ')
print(circle_area(int(input())))
