num = int(input())
my_list = []
for _ in range(num):
    my_list.append(list(map(int, input().split())))
left = 0
right = 0

for i in range(num):
    for j in range(num):

        if i <= j and i < num - 1 - j or i > j and i < num - 1 - j:
            left += my_list[i][j]
        elif i <= j and i > num - 1 - j or i > j and i > num - 1 - j:
            right += my_list[i][j]
if left == right:
    print('YES')
else:
    print('NO')

