# N과 M (9)

n,m=map(int,input().split())

lst=list(map(int,input().split()))
lst.sort()
final=[]
cnt=[]
def dfs():
        
        if len(final)==m:
                print(' '.join(map(str,final)))
                return
        
        for i in lst:
            if len(final)==0:
                final.append(i)
                cnt.append(i)
                dfs()
                final.pop()
            elif i not in final and i not in cnt:
                final.append(i)

                dfs()
                final.pop()
            cnt.append(i)
        cnt=[]

dfs()