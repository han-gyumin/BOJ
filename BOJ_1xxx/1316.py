# 그룹 단어 체커
num=int(input())
arr=[]
j=0
for i in range(num):
    check=input()
    word=len(check)
    while(word!=1):
        
        if check[j]!=check[j+1]:
            arr.append(check[j])
            j+=1
        else:
            j+=1
        word-=1
    if check[-1]!=check[-2]:
        arr.append(1)
    print(arr)
        