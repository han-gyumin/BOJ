# 나머지와 몫이 같은수
import sys
input=sys.stdin.readline

num=int(input())
count=0
for i in range(1,num):
    count+=num*i+i
print(count)