
def read_csv():
    with open('data.csv', encoding='utf-8') as data:
        my_key=data.readline().rstrip().split(',')
        my_data=[i.rstrip().split(',') for i in data.readlines()]
        resolt=[]
        for i in my_data:
            my_dict=dict(zip(my_key,i))
            resolt.append(my_dict)
    return resolt


