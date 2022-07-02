# 누울 자리를 찾아라
n=int(input())
lst=[]
for i in range(n):
    lst.append(input())


num_1=0
num_2=0



for i in range(n):
    index=0
    count=0
    for j in lst[i]:
        
        if j=='.':
            count+=1
        if j=='X':
            if count>=2:
                num_1+=1
            count=0
        if index==n-1 and j=='.' and count>=2:
            num_1+=1
        index+=1

new_lst=[]
new_word=''
for i in range(n):
    for j in range(n):
        new_word+=lst[j][i]
    new_lst.append(new_word)
    new_word=''
    

for i in range(n):
    index=0
    count=0
    for j in new_lst[i]:
        
        if j=='.':
            count+=1
        if j=='X':
            if count>=2:
                num_2+=1
            count=0
        if index==n-1 and j=='.' and count>=2:
            num_2+=1

        index+=1

print(num_1,num_2)
