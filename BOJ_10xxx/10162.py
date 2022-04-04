# 전자레인지
a=300
b=60
c=10
b_a=0
b_b=0
b_c=0
num=int(input())
if num%10!=0:
    print(-1)
elif num>=300:
    while(num>=300):
        num-=300
        b_a+=1
    while(num>=60):
        num-=60
        b_b+=1
    while(num!=0):
        num-=10
        b_c+=1
elif num>=60 and num<300:
    while(num>=60):
        num-=60
        b_b+=1
    while(num!=0):
        num-=10
        b_c+=1
else:
    while(num!=0):
        num-=10
        b_c+=1
if num%10==0:
    print(b_a,b_b,b_c)