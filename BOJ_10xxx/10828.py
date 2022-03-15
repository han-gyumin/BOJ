# 스택
import sys


arr = []


def push(x):
    arr.append(x)


def pop():

    if len(arr) == 0:
        print(-1)
    else:
        print(arr[-1])
        del arr[-1]


def size():
    print(len(arr))


def empty():
    if len(arr) == 0:
        print(1)
    else:
        print(0)


def top():
    if len(arr) != 0:
        print(arr[-1])
    else:
        print(-1)


num = int(sys.stdin.readline())
for i in range(num):
    l = list(map(str, sys.stdin.readline().split()))
    if len(l) != 2:
        a = l[0]
    else:
        a = l[0]
        b = int(l[1])
    if a == "push":
        push(b)
    elif a == "top":
        top()
    elif a == "size":
        size()
    elif a == "pop":
        pop()
    else:
        empty()
