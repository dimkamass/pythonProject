"""
Func 'eagle or tails'

"""

import random


def eagle_tails():
    print("input number of attempts:", end=' ')
    count = int(input())  # количество попыток

    for _ in range(count):
        a = random.randint(1, 2)
        if a == 1:
            print('Орел')
        else:
            print('Решка')


eagle_tails()
