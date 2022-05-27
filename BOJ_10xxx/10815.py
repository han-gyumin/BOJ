# 숫자카드
import sys
n=int(sys.stdin.readline())
lst=set(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
final=set(map(int,sys.stdin.readline().split()))
for i in final:
    if i in lst:
        print(1,end=" ")
    else:
        print(0,end=" ")