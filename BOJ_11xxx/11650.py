# 좌표 정렬하기
num=int(input())
arr=[]
for i in range(num):
    arr.append(list(map(int,input().split())))
arr.sort()
for i in range(len(arr)):
    print(arr[i][0],end=" ")
    print(arr[i][1])    
