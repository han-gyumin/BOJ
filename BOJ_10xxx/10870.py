result=0
def fivo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        result=fivo(n-2)+fivo(n-1)
        return result
num=int(input())
print(fivo(num))