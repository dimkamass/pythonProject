with open('input.txt') as file, open('output.txt','w') as my_output:
    stroka=file.readlines()
    for num,stroka in enumerate(stroka,1):
        my_output.write(f'{num}) {stroka}')