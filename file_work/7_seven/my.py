

for _ in range(int(input())):
    with open(input(),'r') as input_file,open('output.txt','a') as output_file:
        perem=input_file.read()
        output_file.write(perem)

