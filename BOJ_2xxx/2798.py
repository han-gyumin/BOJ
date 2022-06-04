# 블랙잭
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
lst=list(map(int,input().split()))
sum=[]
for i in range(len(lst)-2):
    for j in range(i+1,len(lst)-1):
        for k in range(j+1,len(lst)):
            if(lst[i]+lst[j]+lst[k])<=m:
                sum.append(lst[i]+lst[j]+lst[k])
print(max(sum))