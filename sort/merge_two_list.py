first = [1, 4, 5, 9, 14, 55, 80]
second = [3, 6, 9]


def merge_two_lists(lst1, lst2): # cлияние 2-ух отсортированных списков
    finish_list = []

    while len(lst1) > 0 and len(lst2) > 0:
        if lst1[0] < lst2[0]:
            finish_list.append(lst1[0])
            lst1.pop(0)
        else:
            finish_list.append(lst2[0])
            lst2.pop(0)
    if len(lst1) > 0:
        while len(lst1) > 0:
            finish_list.append(lst1[0])
            lst1.pop(0)
    elif len(lst2) > 0:
        while len(lst2) > 0:
            finish_list.append(lst2[0])
            lst2.pop(0)

    return finish_list


print(merge_two_lists(first, second))
