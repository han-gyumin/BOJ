# 숫자 카드2
import sys

num=int(sys.stdin.readline())
lst=list(map(int,sys.stdin.readline().split()))
n=int(sys.stdin.readline())
lst2=list(map(int,sys.stdin.readline().split()))
final=[]
for i in lst2:
    final.append(lst.count(i))
for i in final:
    print(i,end=" ")