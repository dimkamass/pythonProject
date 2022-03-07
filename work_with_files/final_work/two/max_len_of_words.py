with open('words.txt') as file:
    my_spisok=[i.rstrip() for i in file.readlines()]
    if len(my_spisok)<=10:
        for i in my_spisok:
            print(i)
    else:
        count=-10
        for _ in range(10):
            print(my_spisok[count])
            count+=1

