#분산처리
num = int(input())
c = []
for i in range(num):
    a, b = map(int, input().split())
    a = int(str(a)[-1])
    temp = []
    for i in range(1, b + 1):
        n = int(str(a**i)[-1])
        if n == 0:
            print(10)
            break
        if n not in temp:
            temp.append(n)
            if i == b:
                print(temp[-1])
        else:
            result = temp[b % len(temp) - 1]
            print(result)
            break
