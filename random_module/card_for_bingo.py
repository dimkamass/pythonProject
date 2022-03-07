"""

Print random card for bingi

"""
import random


def card_for_bingo():
    def print_card(list):
        for i in list:
            for j in i:
                print(str(j).ljust(3), end='')
            print()

    my_set = set()
    while len(my_set) < 25:
        my_set.add(random.randint(1, 75))

    finish_list = []
    my_list = list(my_set)
    count = 0
    for i in range(5):
        empty_list = []
        for _ in range(5):
            if count != 12:
                empty_list.append(my_list[0])
                my_list.pop(0)
                count += 1
            else:
                empty_list.append(0)
                count += 1
        finish_list.append(empty_list)
    return print_card(finish_list)


card_for_bingo()
