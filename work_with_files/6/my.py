with open('goats.txt') as goats, open('answer.txt', 'w') as answer:
    my_true=False
    all_goats=list()
    goats_counter=dict()
    while True:
        perem=goats.readline().rstrip()
        if perem=='GOATS':
            my_true=True
        elif perem=='':break
        elif my_true:
            all_goats.append(perem)
            if perem in goats_counter:
                goats_counter[perem]+=1
            else:
                goats_counter[perem]=1
    seven_procent=len(all_goats)/100*7
    finish_list=[]
    for i in goats_counter:
        if goats_counter[i]>seven_procent:
            finish_list.append(i)
    for i in sorted(finish_list):
        print(i,file=answer)





