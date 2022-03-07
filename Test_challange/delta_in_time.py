"""
    Find delta in time

["1:10pm","4:40am","5:00pm"]
Output:230

["10:00am","11:45pm","5:00am","12:01am"]
Output:16
"""


def time_dif(list):
    finish_list = []
    for i in list:
        time = (*map(int, i[:-2].split(':')), i[-2:])
        if time[2] == 'pm' and time[1] != 12:
            finish_list.append((12 + time[0]) * 60 + time[1])
        else:
            if time[2] == 'am' and time[0] == 12:
                finish_list.append((12 + time[0]) * 60 + time[1])
            else:
                finish_list.append((time[0]) * 60 + time[1])

    min_dif = 24 * 60
    for i in finish_list:
        for j in finish_list:
            if 0 < i - j < min_dif:
                min_dif = i - j

    return 'minimal delta is:', min_dif // 60, 'h:', min_dif % 60, 'm'


print(*time_dif(["10:00am", "11:45pm", "5:00am", "12:01am"]))
print(*time_dif(["1:10pm", "4:40am", "5:00pm"]))
