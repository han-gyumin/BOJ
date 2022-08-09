# 주유소
num=int(input())
dis=list(map(int,input().split()))
oil=list(map(int,input().split()))
count=0

count+=dis[0]*oil[0]
del dis[0]
del oil[0]
del oil[-1]
count+=min(oil)*sum(dis)
print(count)