#소인수분해
N=int(input())
num=2
while(True):
    if N==1:
        break
    if N==2:
        print(2)
        break
    if N%num==0:
        print(num)
        N/=num
    elif N%num!=0:
        num+=1
    if N<=num:
        print(num)
        break