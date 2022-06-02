# 단지 번호 붙이기

# dfs로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에 즉시 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y]==1:
        # 해당 노드 방문 처리
        global count
        count+=1
        graph[x][y]=0
        # 상하좌우의 모든 노드들 방문 처리
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    # 애초에 1이거나 방문처리 되어 있는경우 종료
    return False
count=0
n= int(input())
m=n
final=[]
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1
            final.append(count)
            count=0

final.sort()
print(len(final))
for i in final:
    print(i)