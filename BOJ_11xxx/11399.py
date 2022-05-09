# ATM
num=int(input())
lst=sorted(list(map(int,input().split())))
count=0
realcount=0

for i in lst:
    count+=int(i)
    realcount+=count
print(realcount)