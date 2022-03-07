with open('population.txt', encoding='utf-8') as pop:
    spisok = [str(i).rstrip().split() for i in pop.readlines()]
    for i in spisok:
        if i[0][0] == 'G' and int(i[-1]) > 500000:
            print(i[0])
