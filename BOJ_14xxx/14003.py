num=int(input())
lst=list(map(int,input().split()))
final=[]
for i in lst:
    if i not in final:
        final.append(i)

print(len(final))
for i in final:
    print(i,end=" ")