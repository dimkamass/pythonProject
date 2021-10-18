n, m = map(int, input().split())
s = [[0] * m for row in range(n)]
count = 2
right = True
down = False
left = False
up = False
i, j = 0, 0
s[0][0] = 1
if m == 1:
    count = 1
    while count <= n * m:
        s[i][j] = count
        i += 1
        count += 1
else:
    while count <= n * m:

        if right:
            if j + 1 != m:
                if s[i][j + 1] == 0:
                    s[i][j + 1] = count
                    j += 1
            if j + 1 == m or s[i][j + 1] != 0:
                right = False
                down = True
        elif down:
            if i + 1 != n:
                if s[i + 1][j] == 0:
                    s[i + 1][j] = count
                    i += 1
            if i + 1 == n or s[i + 1][j] != 0:
                left = True
                down = False
        elif left:
            if j - 1 >= 0:
                if s[i][j - 1] == 0:
                    s[i][j - 1] = count
                    j -= 1
            if j - 1 < 0 or s[i][j - 1] != 0:
                left = False
                up = True
        elif up:
            if s[i - 1][j] == 0:
                s[i - 1][j] = count
                i -= 1
            if i + 1 == n or s[i - 1][j] != 0:
                right = True
                up = False
        count += 1
for i in range(n):
    for j in range(m):
        print(str(s[i][j]).ljust(3), end='')
    print()
