stroki, stolb = map(int, input().split())
count_stroki, count_stolb = -1, -1
stroka = ''
count=-1
for i in range(stroki):

    if stolb==1:
        count+=1
        for j in range(stolb):
            if count%2==0:
                print(' . ',end='')
            else:
                print(' * ',end='')
        print()
    else:

        for j in range(stolb):

            if count%2==0:

                print(' * ',end='')
                count+=1
            else:
                print(' . ',end='')
                count+=1
        print()


