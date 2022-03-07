"""
    Input() two numbers in format 'num_one num_two'
    Output: chess board num_one * num_two

example:

    input: 5 5
    output:
    . * . * .
    * . * . *
    . * . * .
    * . * . *
    . * . * .

"""


def chess_board(line, column):
    def print_chess_desk(list):
        for i in list:
            print(*i)

    stroka = [([i for i in ('.' * int(column))]) for i in range(int(line))]
    for i in range(len(stroka)):
        for j in range(len(stroka[0])):
            if j % 2 == 1 and i % 2 == 0:
                stroka[i][j] = '*'
            elif j % 2 == 0 and i % 2 == 1:
                stroka[i][j] = '*'
    return print_chess_desk(stroka)


# call func
chess_board(*map(int, input().split()))
