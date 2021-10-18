import random

count = int(input())    # количество попыток

for _ in range(count):
    a=random.randint(1,2)
    if a==1:print('Орел')
    else:print('Решка')