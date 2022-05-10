# 동전 0
n,k=map(int,input().split())
lst=[]
for i in range(n):
    lst.append(int(input()))
lst.reverse()

count=0

for i in lst:
    if i>k:
        continue
    count+=k//i
    k=k%i


print(count)