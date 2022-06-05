# 날짜 계산
import sys
input=sys.stdin.readline
e,s,m=map(int,input().split())
lst_e=list(map(lambda x: x , range(1,16))) 
lst_s=list(map(lambda x: x , range(1,29))) 
lst_m=list(map(lambda x: x , range(1,20))) 


year=0
while(True):
    year+=1
    if e==s and s==m and m==1:
        break
    if e-1==0:
        e=lst_e[-1]
    if s-1==0:
        s=lst_s[-1]
    if m-1==0:
        m=lst_m[-1]
    elif e-1!=0:
        e-=1
    elif s-1!=0:
        s-=1
    elif m-1!=0:
        m-=1
    print(year)
print(year)