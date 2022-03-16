# 요세푸스
from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
q = deque()


for i in range(n):
    q.append(i + 1)

print("<", end="")
while len(q) != 0:
    for i in range(k - 1):
        q.append(q[0])
        q.popleft()
    print(q.popleft(), end="")

    if len(q) != 0:
        print(", ", end="")

print(">")
