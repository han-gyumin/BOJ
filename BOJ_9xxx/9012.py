# 괄호
import sys

num = int(sys.stdin.readline())
arr = []

for i in range(num):
    ps = input()
    for i in ps:
        if i == "(":
            arr.append(i)
        else:
            if len(arr) == 0:
                ans = "NO"
                arr.append("(")
                break
            else:
                arr.pop()
    if len(arr) == 0:
        ans = "YES"
    else:
        ans = "NO"
    print(ans)
    arr = []
