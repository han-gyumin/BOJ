# N과 M (4)

n,m=map(int,input().split())

lst=[]

def dfs():
        if len(lst)==m:
                print(' '.join(map(str,lst)))
                return
        
        for i in range(1,n+1):
            if len(lst)==0:
                lst.append(i)
                dfs()
                lst.pop()
            elif i>=max(lst):
                lst.append(i)
                dfs()
                lst.pop()


dfs()