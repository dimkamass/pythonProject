"""
Задача со сложной формулировкой условия.
    Нужно написать функцию. Она будет принимать список положительных целых чисел. Возвращаться будет список чисел,
имеющий такую же длину, что и исходный.
    Формироваться он должен по следующему принципу.
Под индексом 0 в итоговом списке должна быть сумма чисел исходного списка без числа под индексом 0 в исходном.
Под индексом 1 в итоговом списке должна быть сумма чисел исходного списка без числа под индексом 1 в исходном. И так далее.

Пример для списка [1, 2, 3, 4]; итоговый список, по индексам:

0 ➞ 2+3+4 = 9
1 ➞ 1+3+4 = 8
2 ➞ 1+2+4 = 7
3 ➞ 1+2+3 = 6
Итоговый список — [9, 8, 7, 6]
"""


def func(list):
    finish_list = []
    for i in range(len(list)):
        sum_of_number = 0
        for j in range(len(list)):
            if i != j:
                sum_of_number += list[j]
        finish_list.append(sum_of_number)
    print(finish_list)


func([1, 2, 3, 4])