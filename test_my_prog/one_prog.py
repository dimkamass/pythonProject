from math import pi


def circle_area(radius):
    if radius<0:
        raise ValueError('radius cant be negative')
    elif type(radius) not in (int,float):
        raise TypeError('Type must be int or float')
    else:
        return pi*radius**2
circle_area(-1)
