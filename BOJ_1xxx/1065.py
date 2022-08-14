# 한수
num=int(input())

arr=[]
def hansoo(num):
    count=0
    for i in range(1,num+1):
        if len(str(i))<=2:
            count+=1
        elif len(str(i))==3:
            if (int(str(i)[2])-int(str(i)[1]))==(int(str(i)[1])-int(str(i)[0])):
                count+=1
        else:
            pass
                
    print(count)
hansoo(num)