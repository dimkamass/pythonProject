"""
    Input() two numbers in format 'num_one num_two'
    Output: snake matrix num_one * num_two in range(1,num_one * num_two)

example:

    input: 5 5
    output:
    1  2  3  4  5
    10 9  8  7  6
    11 12 13 14 15
    20 19 18 17 16
    21 22 23 24 25

"""


def snake_matrix(num_one, num_two):
    def print_matrix(num_one, num_two, list):
        for i in range(num_one):
            for j in range(num_two):
                print(str(s[i][j]).ljust(3), end='')
            print()

    s = []
    a = []
    count = 1
    for i in range(num_one):
        for j in range(num_two):
            a.append(count)
            count += 1
        s.append(a)
        a = []
        if (i + 1) % 2 == 0:
            s[i].sort(reverse=True)

    return print_matrix(num_one, num_two, s)


snake_matrix(*map(int, input().split()))
