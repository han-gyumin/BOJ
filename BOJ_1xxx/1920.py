# 수찾기
a=int(input())
arr=[]
arr.append(list(map(int, input().split())))
b=int(input())
arr2=[]
arr2.append(list(map(int, input().split())))
for i in arr2[0]:
    if i in arr[0]:
        print("1")
    else:
        print("0")
