from functools import reduce

with open('file.txt', encoding='utf-8') as file:
    lines = [i.rstrip() for i in file.readlines()]
    count_words = reduce(lambda y, x: len(str(x).split()) + y, lines, 0)
    letters = ''.join(lines)
    finish = list(filter(lambda x: x if str(x).isalpha() else False, letters))
print(f"""Input file contains:
{len(finish)} letters 
{count_words} words 
{len(lines)} lines
""")
