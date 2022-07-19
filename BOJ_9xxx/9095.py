# 1,2,3 더하기
t=int(input())
def hap(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    else:
        return hap(n-3)+hap(n-2)+hap(n-1)

for i in range(t):
    n=int(input())
    print(hap(n))