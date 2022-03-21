# 오븐시계
import sys

a, b = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
if b + c > 59:
    if (a + (b + c) // 60) >= 24:
        print(((b + c) // 60) - (23 - a) - 1, (b + c) % 60)
    else:
        print(((b + c) // 60) + a, (b + c) % 60)
else:
    print(a, b + c)
