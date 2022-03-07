"""
    Create email in format username@domain
    Sorted in alphabet

"""

emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}


#   сортировка в алфавитном порядке в формате вывода username@domain


def create_email(list_one):
    finish_list = []

    def print_sorted_list_of_email(some_list):
        for i in sorted(finish_list):
            print(i)

    for i in list_one:
        for j in list_one[i]:
            finish_list.append(f'{j}@{i}')
    return print_sorted_list_of_email(finish_list)


create_email(emails)
