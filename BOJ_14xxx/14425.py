# 문자열집합
import sys
input=sys.stdin.readline
n,m=map(int,input().split())

count=0
lst={input().rstrip() for _ in range(n)}

for i in range(m):
    string=input().rstrip()
    if string in lst:
        count+=1

print(count)
