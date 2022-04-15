# 3의 배수
num=int(input())
count=0
arr=[]
while len(str(num))!=1:
    for i in str(num):
        arr.append(i)
    count+=1
    num=0
    for i in arr:
        num+=int(i)
    arr.clear()


print(count)
if num%3==0:
    print("YES")
else:
    print('NO')

