import random
import string

my_list1 = list(string.ascii_letters + string.digits)
my_list = []
bad_symbol = '01iIoOlL'
for i in my_list1:
    if i not in bad_symbol:
        my_list.append(i)

count = int(input())
length = int(input())


def generate_password(length):
    password = ''
    my_True = True
    while my_True:
        password = ''
        for _ in range(length):
            password += str(random.choice(my_list))
        if set(string.digits).intersection(password) and set(string.ascii_lowercase).intersection(password) and set(
                string.ascii_uppercase).intersection(password):
            my_True = False

    return password


def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))


generate_passwords(count, length)
