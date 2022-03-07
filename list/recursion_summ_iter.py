"""

    Напишите функцию. Она должна принимать число, цифры которого будут перемножаться между собой,
пока  не  получится  однозначное  число. Функция  должна  вернуть  количество операций умножения,
которые  потребовались  для  получения  этого  однозначного  числа.
"""

from functools import *

def how_many(input: str,):
    if int(input)<=9:
        return 1
    else:

        return 1+how_many(str(reduce(lambda x,y:x*y,map(int,input))))

print(how_many('1'))
print(how_many("14"))
print(how_many("999"))
