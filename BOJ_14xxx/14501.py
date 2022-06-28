# 퇴사
import sys
input=sys.stdin.readline
n=int(input())
lst_t=[]
lst_p=[]
for i in range(n):
    a,b=map(int,input().split())
    lst_t.append(a)
    lst_p.append(b)
print(lst_t)
print(lst_p)