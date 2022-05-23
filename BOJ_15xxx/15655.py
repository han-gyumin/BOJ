# N과 M (6)

n,m=map(int,input().split())

lst=list(map(int,input().split()))
lst.sort()
final=[]
def dfs():
        if len(final)==m:
                print(' '.join(map(str,final)))
                return
        
        for i in lst:
            if len(final)==0:
                final.append(i)
                dfs()
                final.pop()
            else :
                final.append(i)
                dfs()
                final.pop()


dfs()