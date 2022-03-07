"""
Напишите функцию, которая будет принимать начальное и конечное значения
диапазона чисел и возвращать наибольшее простое число в этом диапазоне.


"""


def find_simple_num(a, b):
    if b > a:
        list_of_number = [i for i in range(a, b + 1)]
    else:
        list_of_number = [i for i in range(b, a + 1)]
    list_of_number.reverse()
    for i in list_of_number:
        count = 0
        for j in range(1, i):
            if i % j == 0:
                count += 1
        if count == 1:
            print(f'simple is {i}')
            break


find_simple_num(2, 10)
find_simple_num(10, 2)
find_simple_num(4, 24)
