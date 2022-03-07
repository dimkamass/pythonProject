"""
Sample Input:
4
1 2 3 1
4 5 6 4
7 8 9 7
1 2 3 8

Sample Output:
1 4 7 1
2 5 8 2
3 6 9 3
1 4 7 8

"""
def transpose_matrix():
    num = int(input())
    my_list = []
    for _ in range(num):
        my_list.append(list(map(int, input().split())))
    for i in range(num):
        for j in range(num):
            print(my_list[j][i], end=' ')
        print()
transpose_matrix()

