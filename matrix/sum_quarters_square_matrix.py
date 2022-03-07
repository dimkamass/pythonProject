"""
    Func() sum of quarters in square matrix
input():
4
1 2 3 4
1 2 3 4
4 5 6 5
1 2 3 4
Output:
Верхняя четверть: 5
Правая четверть: 9
Нижняя четверть: 5
Левая четверть: 5

"""
def sum_of_quarters():
    def print_matrix(dict):
        for i in dict:
            print(i, dict[i])

    side = int(input())
    s = []
    for _ in range(side):
        a = list(map(int, input().split()))
        s.append(a)
    final_dict = {'Верхняя четверть:': 0, 'Правая четверть:': 0, 'Нижняя четверть:': 0, 'Левая четверть:': 0}
    if side % 2 == 0:
        for i in range(side):
            for j in range(side):
                if i > j and i < side - 1 - j:
                    final_dict['Левая четверть:'] += s[i][j]
                elif i < j and i > side - 1 - j:
                    final_dict['Правая четверть:'] += s[i][j]
                elif i < j and i < side - 1 - j:
                    final_dict['Верхняя четверть:'] += s[i][j]
                elif i > j and i > side - 1 - j:
                    final_dict['Нижняя четверть:'] += s[i][j]
    else:
        for i in range(side):
            for j in range(side):
                if i > j and i < side - 1 - j:
                    final_dict['Левая четверть:'] += s[i][j]
                elif i < j and i > side - 1 - j:
                    final_dict['Правая четверть:'] += s[i][j]
                elif i < j and i < side - 1 - j:
                    final_dict['Верхняя четверть:'] += s[i][j]
                elif i > j and i > side - 1 - j:
                    final_dict['Нижняя четверть:'] += s[i][j]

    return print_matrix(final_dict)
sum_of_quarters()