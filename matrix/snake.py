n, m = map(int, input().split())
s = []
a = []
count = 1
for i in range(n):
    for j in range(m):
        a.append(count)
        count += 1
    s.append(a)
    a = []
    if (i + 1) % 2 == 0:
        s[i].sort(reverse=True)
for i in range(n):
    for j in range(m):
        print(str(s[i][j]).ljust(3), end='')
    print()
