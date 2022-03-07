"""

    Horse move options

example:

    input: 'f7'
    output: try


"""
coor_j = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
coor_i = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}


def horse_move(position):
    def print_desk(list):
        for i in list:
            print(*i)

    k = 7  # размер квадратной матрицы
    desk = [['.'] * (k + 1) for a in range(8)]

    i = coor_i[position[1]]
    j = coor_j[position[0]]

    desk[i][j] = 'H'
    if i in range(2, k + 1) and j in range(0, k):  # up_right
        desk[i - 2][j + 1] = '*'
    if i in range(2, k + 1) and j in range(1, k + 1):  # up_left=True
        desk[i - 2][j - 1] = '*'
    if i in range(0, k - 1) and j in range(0, k):  # down_right=True
        desk[i + 2][j + 1] = '*'
    if i in range(0, k - 1) and j in range(1, k + 1):  # down_left=True
        desk[i + 2][j - 1] = '*'
    if i in range(1, k + 1) and j in range(2, k + 1):  # left_up=True
        desk[i - 1][j - 2] = '*'
    if i in range(0, k) and j in range(2, k + 1):  # left_down=True
        desk[i + 1][j - 2] = '*'
    if i in range(1, k + 1) and j in range(0, k - 1):  # right_up=True
        desk[i - 1][j + 2] = '*'
    if i in range(0, k) and j in range(0, k - 1):  # right_down=True
        desk[i + 1][j + 2] = '*'
    return print_desk(desk)


horse_move(input())
