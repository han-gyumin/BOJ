#나누기
n = int(input())
f = int(input())
nn = n - int(str(n)[-2:])
if nn % f == 0:
    print(str(nn)[-2:])
else:
    while True:
        nn += 1
        if nn % f == 0:
            print(str(nn)[-2:])
            break
