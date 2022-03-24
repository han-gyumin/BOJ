# 나머지
import sys

arr = []
arr2 = []
for i in range(10):
    arr.append(int(sys.stdin.readline()) % 42)
for i in arr:
    if i not in arr2:
        arr2.append(i)
print(len(arr2))
