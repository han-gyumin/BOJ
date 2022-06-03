# 시험 감독
import sys
input=sys.stdin.readline

n=int(input())
lst_a=list(map(int,input().split()))
b,c=map(int,input().split())

count=0
for i in lst_a:
    if i<=b:
        count+=1
        pass
    elif (i-b)<=c:
        count+=2
    elif(i-b)%c==0:
        count+=((i-b)//c+1)
    else:
        count+=((i-b)//c+2)

print(count)