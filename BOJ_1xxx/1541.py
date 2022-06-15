# 잃어버린 괄호
from operator import index


n=input()
m=n.replace('+','-')
lst2=[]
lst_index=[]
for i in n:
    if i=='+' or i=='-':
        lst2.append(i)
lst=list(map(str,m.split('-')))
for i in range(len(lst2)):
    lst.insert(2*i+1,lst2[i])
sum=0
for i in range(1,len(lst),2):
    if lst[i]=='+':
        if i-1 not in lst_index:
            lst_index.append(i-1)
            sum+=int(lst[i-1])
        if i+1 not in lst_index:
            lst_index.append(i+1)
            sum+=int(lst[i+1])
print(sum)
print(lst)
print(lst2)