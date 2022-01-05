from collections import deque

# if name[-1]='m', its mean that this person is mango seller.
# else: no mango seller

my_dict = {'you': ['Bob', 'Clar', 'Alice'],
           'Bob': ['Anuj', 'Peggi'],
           'Alice': ['Peggi'],
           'Clar': ['Tom', 'Jony'],
           'Anuj': [],
           'Peggi': [],
           'Jony': [],
           'Tom': []}


def searc(name):
    search_queue = deque()
    search_queue += my_dict[name]
    print(search_queue)
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person[-1] == 'm':
                print(person + ' is a mango seller')
                return False

            else:
                search_queue += my_dict[person]
                searched.append(person)
    print('No mango seller')


searc('you')
