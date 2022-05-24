# 모두의 마블
import sys

num=int(sys.stdin.readline())
lst=list(map(int,sys.stdin.readline().split()))
maximum=max(lst)
index=lst.index(maximum)
count=0
del lst[index]
count=sum(lst)+maximum*len(lst)
print(count)