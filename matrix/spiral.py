"""
    Input() two numbers in format 'num_one num_two'
    Output: spiral matrix num_one * num_two in range(1,num_one * num_two)

example:

    input: 5 5
    output:
    1  2  3  4  5
    10 9  8  7  6
    11 12 13 14 15
    20 19 18 17 16
    21 22 23 24 25

"""


def spiral_matrix(num_one, num_two):
    s = [[0] * num_two for row in range(num_one)]
    count = 2
    right = True
    down = False
    left = False
    up = False
    i, j = 0, 0
    s[0][0] = 1
    if num_two == 1:
        count = 1
        while count <= num_one * num_two:
            s[i][j] = count
            i += 1
            count += 1
    else:
        while count <= num_one * num_two:

            if right:
                if j + 1 != num_two:
                    if s[i][j + 1] == 0:
                        s[i][j + 1] = count
                        j += 1
                if j + 1 == num_two or s[i][j + 1] != 0:
                    right = False
                    down = True
            elif down:
                if i + 1 != num_one:
                    if s[i + 1][j] == 0:
                        s[i + 1][j] = count
                        i += 1
                if i + 1 == num_one or s[i + 1][j] != 0:
                    left = True
                    down = False
            elif left:
                if j - 1 >= 0:
                    if s[i][j - 1] == 0:
                        s[i][j - 1] = count
                        j -= 1
                if j - 1 < 0 or s[i][j - 1] != 0:
                    left = False
                    up = True
            elif up:
                if s[i - 1][j] == 0:
                    s[i - 1][j] = count
                    i -= 1
                if i + 1 == num_one or s[i - 1][j] != 0:
                    right = True
                    up = False
            count += 1
    for i in range(num_one):
        for j in range(num_two):
            print(str(s[i][j]).ljust(3), end='')
        print()

# called func
spiral_matrix(*map(int, input().split()))
