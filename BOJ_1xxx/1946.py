# 신입사원
import sys
n=int(sys.stdin.readline())

for i in range(n):
    num=int(sys.stdin.readline())
    lst=[]*num
    lst_check=[]
    for j in range(num):
        lst.append(list(map(int,input().split())))
    lst.sort()
    min=lst[0][1]
    count=1
    for j in range(1,num):
        if lst[j][1]<min:
            min=lst[j][1]
            count+=1
        
        


    print(count)


# n = int(input())
# count = 0
# for i in range(n) :
#     array= []
#     result = 1    
#     m = int(input())
#     for i in range(m) : 
#         array.append(tuple(map(int,input().split())))
#     array.sort() 
#     print(array)

#     min = array[0][1]

#     for j in range(1,m) : 
#         if array[j][1] < min : 
#             min = array[j][1]
#             result += 1
    
#     count +=1
    
#     print(result)