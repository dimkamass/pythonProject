

def witch_more(list):
    return sum(1 if i > 0 else -1 if i < 0 else 0 if i==0 else 'hello' for i in set(list)) > 0


print(witch_more([1, 1, 1, 1, -3, -4]))