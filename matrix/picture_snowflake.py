"""
draw snowflake

example:
input(): 5
output:
* . * . *
. * * * .
* * * * *
. * * * .
* . * . *

"""
def draw_snowflake():
    num = int(input())
    for i in range(num):
        half_list = []
        for j in range(num):
            if i == j or i == num // 2 or j == num // 2 or i == num - 1 - j:
                half_list.append('*')
            else:
                half_list.append('.')
        print(*half_list)
draw_snowflake()