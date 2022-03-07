with open('grades.txt') as file:
    my_list=[i.rstrip().split() for i in file.readlines()]
    print(len(list(filter(lambda x:x if int(x[1])>=65 and int(x[2])>=65 and int(x[3])>=65 else False,my_list))))
