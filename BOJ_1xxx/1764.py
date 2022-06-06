# 듣보잡
import sys
input=sys.stdin.readline

n,m = map(int,input().split())
lst_hear=[]
lst_see=[]
for i in range(n):
    lst_hear.append(input().rstrip())
for i in range(m):
    lst_see.append(input().rstrip())

count=0
lst=[]
set1=set(lst_hear)
set2=set(lst_see)
lst=list(set1&set2)
print(len(lst))
lst.sort()
for i in lst:
    print(i)
