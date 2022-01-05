spisok=[15,12,11,33,32,1,5,6,7,8,9,12,28,25]


def quik_sort(list):
    if len(list)<2:
        return list
    else:
        zero_elem=list[0]
        more_thet_zero=[]
        less_then_zero=[]
        for i in range(1,len(list)):
            if list[i]>zero_elem:
                more_thet_zero.append(list[i])
            else:
                less_then_zero.append(list[i])
        return quik_sort(less_then_zero)+[zero_elem]+quik_sort(more_thet_zero)
print(quik_sort(spisok))