emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}


#   сортировка в алфавитном порядке в формате вывода username@domain
finish_list = []
for i in emails:
    for j in emails[i]:
        finish_list.append(f'{j}@{i}')
for i in sorted(finish_list):
    print(i)
