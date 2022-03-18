# 제로
import sys

num = int(sys.stdin.readline())
a = []
cnt = 0
for i in range(num):
    cnt = int(sys.stdin.readline())
    if cnt == 0:
        a.pop()
    else:
        a.append(cnt)
print(sum(a))
