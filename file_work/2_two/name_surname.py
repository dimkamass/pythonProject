from random import randint

with open('first_names.txt', encoding='utf-8') as first_name, open('last_names.txt', encoding='utf-8') as last_name:
    name = [i.rstrip() for i in first_name.readlines()]
    surname = [i.rstrip() for i in last_name.readlines()]
for i in range(3):
    print(name[randint(0, len(name) - 1)], surname[randint(0, len(surname) - 1)])
