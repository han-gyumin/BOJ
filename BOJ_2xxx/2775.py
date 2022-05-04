num=int(input())
arr=[[]]
for i in range(1,15):
    arr[0].append(i)



for i in range(num):
    resident=0
    n=int(input())
    k=int(input())
    if n==0:
        resident=arr[0][k-1]
    print(resident)