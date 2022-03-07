j=set(input())
s=input()
count=0
for i in j:
    for q in s:
        if i==q:
            count+=1
print(count)
print(j)
