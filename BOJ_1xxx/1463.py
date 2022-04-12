# 1로 만들기
x=int(input())
count=0
while(x!=1):
    if (x-1)%3==0:
        x-=1
        count+=1
        pass
    elif x%3==0:
        x/=3
        count+=1
        pass
    elif x%2==0:
        x/=2
        count+=1
        pass
    else:
        x-=1
        count+=1
        pass
print(count)