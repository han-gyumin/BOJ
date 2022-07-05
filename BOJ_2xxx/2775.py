# 부녀회장이 될테야
num = int(input())

for _ in range(num):  
    k = int(input())  
    n = int(input()) 
    lst_0 = [x for x in range(1, n+1)] 
    for i in range(k):  
        for j in range(1, n):  
            lst_0[j] += lst_0[j-1]  
    print(lst_0[-1])  