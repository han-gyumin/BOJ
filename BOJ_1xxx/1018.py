n, m = map(int, input().split())
lst=[]
cnt=[]
for i in range(n):
    lst.append([])
    ip=input()
    for j in range(m):
        lst[i].append(ip[j])



for i in range(m-8+1):
    for j in range(n-8+1):
        count=0
        for k in range(8):
            for l in range(8):
                if lst[j][i]=='W':
                    if (l+k+i+j)%2==(i+j)%2 and lst[k+j][l+i]=='B':
                        count+=1
                    elif (l+k+i+j)%2!=(i+j)%2 and lst[k+j][l+i]=='W':
                        count+=1
                elif lst[j][i]=='B':
                    if (l+k+i+j)%2==(i+j)%2 and lst[k+j][l+i]=='W':
                        count+=1
                    if (l+k+i+j)%2!=(i+j)%2 and lst[k+j][l+i]=='B':
                        count+=1
        if count>32:
            count=64-count
        cnt.append(count)


print(min(cnt))


