# 수리공 항승
n,l=map(int,input().split())

lst=list(map(float,input().split()))
lst.sort()
count=0

lst2=[]
for i in lst:
    if len(lst2) !=0 and (min(lst2)<i and max(lst2)>i) :
        continue
    else:
        lst2=[]
        lst2.append(i-0.5)
        lst2.append(i+l-0.5)
        count+=1

print(count)