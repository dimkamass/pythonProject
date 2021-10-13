# put your python code here
n = int(input())
s = []
for _ in range(n):
    a = list(map(int, input().split()))
    s.append(a)
final_list = []
final_dict = {'Верхняя четверть:': 0, 'Правая четверть:': 0, 'Нижняя четверть:': 0, 'Левая четверть:': 0}
y = 0
if n % 2 == 0:
    for i in range(n):
        for j in range(n):
            if i > j and i < n - 1 - j:
                final_dict['Левая четверть:'] += s[i][j]
            elif i < j and i > n - 1 - j:
                final_dict['Правая четверть:'] += s[i][j]
            elif i < j and i < n - 1 - j:
                final_dict['Верхняя четверть:'] += s[i][j]
            elif i > j and i > n - 1 - j:
                final_dict['Нижняя четверть:'] += s[i][j]
else:
    for i in range(n):
        for j in range(n):
            if i > j and i < n - 1 - j:
                final_dict['Левая четверть:'] += s[i][j]
            elif i < j and i > n - 1 - j:
                final_dict['Правая четверть:'] += s[i][j]
            elif i < j and i < n - 1 - j:
                final_dict['Верхняя четверть:'] += s[i][j]
            elif i > j and i > n - 1 - j:
                final_dict['Нижняя четверть:'] += s[i][j]

for i in final_dict:
    print(i, final_dict[i])
