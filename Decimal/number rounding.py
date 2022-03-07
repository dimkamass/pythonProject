"""'
    This function:
        input(): float
        :return decimal with number rounding ",00"

"""

from decimal import *


def map(function, items):
    result = []
    for item in items:
        result.append(function(Decimal(item).quantize(Decimal('1.00'))))
    return result


numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828,
           1.41546]
for i in map(float, numbers):
    print(i)
