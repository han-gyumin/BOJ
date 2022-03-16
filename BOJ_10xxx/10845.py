# 큐
from collections import deque
import sys


q = deque()

num = int(sys.stdin.readline())
for i in range(num):
    l = list(map(str, sys.stdin.readline().split()))
    if len(l) != 2:
        a = l[0]
    else:
        a = l[0]
        b = int(l[1])

    if a == "push":
        q.append(b)
    elif a == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif a == "size":
        print(len(q))
    elif a == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif a == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif a == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
