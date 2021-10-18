import random

s = []
for _ in range(30):
    a = random.randint(1, 49)
    if a not in s:
        s.append(a)
s = sorted(s)

for i in range(7):
    print(s[i], end=' ')
