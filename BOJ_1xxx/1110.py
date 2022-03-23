# 더하기 사이클
arr = []
import sys

num = int(sys.stdin.readline())

num2 = num
cnt = 0
while True:

    if num < 10:
        num = num * 10 + num
    else:
        num = num % 10 * 10 + (num // 10 + num % 10) % 10
    cnt += 1
    if num == num2:
        break
print(cnt)
