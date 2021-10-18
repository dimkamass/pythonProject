spisok = [100,1, 4, -1, -10, 16, -2, -4, -6, 8, 20, 0]


def intersection_sort(list): # сортировка вставками
    len_list = len(list)
    for i in range(1, len_list):
        for j in range(i, 0, -1):
            if spisok[j] < spisok[j - 1]:
                spisok[j], spisok[j - 1] = spisok[j - 1], spisok[j]
    return list


print(intersection_sort(spisok))
