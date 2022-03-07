"""
    В   последовательности   Перрена   каждое   число   представляет   собой   сумму   двух   чисел,
стоящих перед этим числом на второй и третьей позиции.Первые три числа последовательности — 3, 0, 2.
    Выглядит последовательность так:
perrin(1) ➞ 0
perrin(8) ➞ 10
perrin(26) ➞ 1497

"""


def return_num(index):
    perren_list = [3, 0, 2]
    if index <= 2:
        return perren_list[index]
    else:
        for _ in range(index - 2):
            perren_list.append(perren_list[-2] + perren_list[-3])
    return perren_list[index]


def return_num_recursion(index):
    perren_list = [3, 0, 2]
    if index <= 2:
        return perren_list[index]
    return return_num_recursion(index - 2) + return_num_recursion(index - 3)


print(return_num(26))
print(return_num_recursion(26))
