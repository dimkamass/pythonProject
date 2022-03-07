"""
Sample Input:
5

Sample Output:

0 1 2 3 4
1 0 1 2 3
2 1 0 1 2
3 2 1 0 1
4 3 2 1 0
"""
def square_matrix():
    num = int(input())

    finish_list = []

    for i in range(num):
        first_list = [i for i in range(num)]
        for j in range(i):
            first_list.pop()
            first_list.insert(0, j + 1)
        finish_list.append(first_list)
    for i in finish_list:
        print(*i)
square_matrix()