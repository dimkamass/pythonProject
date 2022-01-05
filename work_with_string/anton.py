anton = 'anton'
finish_list = []
count = 1
for _ in range(int(input())):
    anton = [i for i in 'anton']
    for j in input():
        if len(anton) == 0:
            finish_list.append(count)
            break
        elif j == anton[0]:
            anton.pop(0)
            if len(anton) == 0:
                finish_list.append(count)
                break

    count += 1
print(*finish_list)

'''
if 'anton' in word:
    output line number
    
for example:
    9
    osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
    anton
    aoooooooooontooooo
    elelelelelelelelelel
    ntoneeee
    tonee
    253235235a5323352n25235352t253523523235oo235523523523n
    antoooooooooooooooooooooooooooooooooooooooooooooooooooon
    unton

'''
