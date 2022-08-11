# 킹, 퀸, 룩, 비숍, 나이트, 폰
lst=[1,1,2,2,2,8]
lst_i=list(map(int,input().split()))
lst_new=[]
for i in range(len(lst_i)):
    lst_new.append(lst[i]-lst_i[i])

for i in lst_new:
    print(i,end=' ')