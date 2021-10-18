count_stroki,len_stroki = map(int, input().split())
stroka = [([i for i in ('.' * int(len_stroki))]) for i in range(int(count_stroki))]
for i in range(len(stroka)):
    for j in range(len(stroka[0])):
        if j % 2 == 1 and i % 2 == 0:
            stroka[i][j] = '*'
        elif j % 2 == 0 and i % 2 == 1:
            stroka[i][j] = '*'
for i in stroka:
    print(*i)
