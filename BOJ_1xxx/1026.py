# 보물
num=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))


a.sort()
b.sort()
b.reverse()

count=0

for i in range(len(a)):
    count+=a[i]*b[i]

print(count)