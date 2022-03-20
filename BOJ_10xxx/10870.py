# 피보나치 수열
def fivo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fivo(x - 1) + fivo(x - 2)


num = int(input())

print(fivo(num))
