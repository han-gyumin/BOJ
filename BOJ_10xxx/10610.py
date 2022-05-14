# 30
num=input()

lst=[]
final=[]
for i in range(len(num)):
    lst.append(int(num[i]))

lst.sort()
lst.reverse()
for i in range(len(lst)):
    final.append(str(lst[i]))

if int(num)%3==0 and '0'in num:
    print(''.join(final))
else:print(-1)