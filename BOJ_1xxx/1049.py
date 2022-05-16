# 기타줄
n,m=map(int,input().split())
lst_1=[]
lst_sum=[]

for i in range(m):
    brand=list(map(int,input().split()))
    lst_sum.append(brand[0])
    lst_1.append(brand[1])

if min(lst_1)*n<min(lst_sum) or min(lst_sum)>min(lst_1)*6:
    print(min(lst_1)*n)
else:
    if min(lst_sum)*(n//6)+min(lst_1)*(n%6)>min(lst_sum)*(n//6+1):
        print(min(lst_sum)*(n//6+1))
    else:
        print(min(lst_sum)*(n//6)+min(lst_1)*(n%6))