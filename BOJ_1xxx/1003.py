# 피보나치 함수
from pickle import EMPTY_LIST


lst=[0,0]
final=[]
dp=[[]]*50
def fibo(n):
    if dp[n]>0:
        return dp[n]
    elif n==0:
        lst[0]+=1
        
    elif n==1:
        lst[1]+=1
        
    else:
        fibo(n-1)+fibo(n-2)
    dp[n].append([lst[0],lst[1]])
    return dp[n]

    
print(fibo(3))
# for i in range(int(input())):
#     n=int(input())
#     for j in fibo(n):
#         print(j,end=" ")

#     lst=[0,0]
#     print()