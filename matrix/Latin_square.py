"""
Латинским квадратом порядка n называется квадратная матрица размером n×n,
каждая строка и каждый столбец которой содержат все числа от 1 до n.
Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.

Input:
4
2 3 4 1
3 4 1 2
4 1 2 3
1 2 3 4

Output:
YES

"""
def latin_matrix():
    num = int(input())
    my_list = []
    for _ in range(num):
        my_list.append(list(map(int, input().split())))
    my_set = {int(i) for i in range(1, num + 1)}

    lat_square = True
    for i in my_list:
        if set(i) != my_set:
            lat_square = False
    for i in range(num):
        inner_set = set()
        for j in range(num):
            inner_set.add(my_list[j][i])
        if inner_set != my_set:
            lat_square = False
        inner_set.clear()
    if lat_square:
        print('YES')
    else:
        print('NO')
latin_matrix()