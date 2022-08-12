x,y=map(int,input().split())
z=int(y/x*100)
temp=z

count=0
while(temp==z):
    x+=1
    y+=1
    z=int(y/x*100)
    count+=1

print(count)