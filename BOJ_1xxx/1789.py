# 수들의 합

s=int(input())
# for i in range(s):
    
#     if sum(lst)+i<s and s-sum(lst)-i>i:
#         lst.append(i)
    
#     if s-(sum(lst)+i)<i:
#         lst.append(s-(sum(lst)+i))
#         print(len(lst)-1)
#         break

for i in range(s):
    if s==1:
        print(1)
        break
    elif s==2:
        print(1)
        break
    elif s==3:
        print(2)
        break
    if i*(i+1)>2*s:
        print(i-1)
        break