spisok = [-1, -5, 10, 0, 2, -6, 9, 11]


def buble_sort(list):    # сортировка пузырьком
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


print(buble_sort(spisok))
