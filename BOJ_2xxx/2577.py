# 숫자의 개수
import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
num = a * b * c
arr = [0] * 10
for i in range(len(str(num))):
    arr[int(str(num)[i])] += 1
for i in arr:
    print(i)
