from math import sqrt


class Point:
    def set_point(self, x_cord, y_cord):
        self.x = x_cord
        self.y = y_cord

    def get_distance(one_point, two_point):
        if isinstance(one_point, Point) and isinstance(two_point, Point):
            return sqrt((one_point.x - two_point.x) ** 2 + (one_point.y - two_point.y) ** 2)
        else:
            print('its not a point')
