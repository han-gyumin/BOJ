n, m = map(int, input().split())
arr=[]
count=0
count2=[]
for i in range(m):
    arr.append(input())
for i in range(m-7):
    for j in range(n-7):
        for k in range(8):
            for a in range(8):
                if arr[i][j]=='W':
                    if (i+j)%2==0:
                        if (a+k)%2==0 and arr[k][a]=='B':
                            count+=1
                        elif (a+k)%2==1 and arr[k][a]=='W':
                            count+=1
                    if(i+j)%2==1:
                        if(a+k)%2==0 and arr[k][a]=='W':
                            count+=1
                        elif(a+k)%2==1 and arr[k][a]=='B':
                            count+=1
                if arr[i][j]=='B':
                    if (i+j)%2==0:
                        if (a+k)%2==0 and arr[k][a]=='W':
                            count+=1
                        elif (a+k)%2==1 and arr[k][a]=='B':
                            count+=1
                    if(i+j)%2==1:
                        if(a+k)%2==0 and arr[k][a]=='B':
                            count+=1
                        elif(a+k)%2==1 and arr[k][a]=='W':
                            count+=1
        if count>32:
            count=64-count
        count2.append(count)
        count=0
    print(i, j)
print(count2)
print(min(count2))