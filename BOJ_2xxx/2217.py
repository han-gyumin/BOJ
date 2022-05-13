# 로프
num=int(input())
lst=[]
for i in range(num):
    lst.append(int(input()))
lst.sort()
lst.reverse()
lst2=[]
for i in range(len(lst)):
    lst2.append(lst[i]*(i+1))

print(max(lst2))