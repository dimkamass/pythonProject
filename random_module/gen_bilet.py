"""
generation lucky bilet
"""


import random

def gen_bil():
    def print_bil(list):
        for i in range(7):
            print(list[i], end=' ')

    list_with_numbers = []
    for _ in range(30):
        a = random.randint(1, 49)
        if a not in list_with_numbers:
            list_with_numbers.append(a)
    list_with_numbers = sorted(list_with_numbers)

    return print_bil(list_with_numbers)

gen_bil()


