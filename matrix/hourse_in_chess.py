coor_j = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
coor_i = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
#n = input()

# for example, num will be 'f7'
n='f7'

k = 7  # размер квадратной матрицы
s = [['.'] * (k + 1) for a in range(8)]

i = coor_i[n[1]]
j = coor_j[n[0]]

s[i][j] = 'N'
if i in range(2, k + 1) and j in range(0, k):  # up_right
    s[i - 2][j + 1] = '*'
if i in range(2, k + 1) and j in range(1, k + 1):  # up_left=True
    s[i - 2][j - 1] = '*'
if i in range(0, k - 1) and j in range(0, k):  # down_right=True
    s[i + 2][j + 1] = '*'
if i in range(0, k - 1) and j in range(1, k + 1):  # down_left=True
    s[i + 2][j - 1] = '*'
if i in range(1, k + 1) and j in range(2, k + 1):  # left_up=True
    s[i - 1][j - 2] = '*'
if i in range(0, k) and j in range(2, k + 1):  # left_down=True
    s[i + 1][j - 2] = '*'
if i in range(1, k + 1) and j in range(0, k - 1):  # right_up=True
    s[i - 1][j + 2] = '*'
if i in range(0, k) and j in range(0, k - 1):  # right_down=True
    s[i + 1][j + 2] = '*'
for i in s:
    print(*i)
