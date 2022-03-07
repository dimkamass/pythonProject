def time_count(input_time, exit_time):
    exit = list(map(int, exit_time.split(':')))
    inp = list(map(int, input_time.split(':')))
    return exit[0] * 60 + exit[1] - (inp[0] * 60 + inp[1])


with open('logfile.txt') as file,open('output.txt','w') as go_out:
    data = [i.rstrip().split(', ') for i in file.readlines()]
    for i in data:
        if time_count(i[1], i[2]) >= 60:
            print(i[0],file=go_out)
