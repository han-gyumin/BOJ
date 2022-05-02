# import heapq
# import sys

# heap=[]
# max_heap=[]
# num=sys.stdin.readline()
# for i in range(num):
#     n=int(sys.stdin.readline())
#     if n!=0:
#         heapq.heappush(heap,n)
#         heapq.heappush(max_heap, (-item, item))
#     else:


student_dict = {'Name': 'Emma', 'Info': {'Age': 20, 'Birth': '2003.09.14', 'Height': '163.5cm'}, 'Major': 'EE'}

# height를 구하는 코드를 작성하세요: your code here

height=student_dict['Info']['Height'][0:5]

# b_month를 구하는 코드를 작성하세요: your code here
b_month=student_dict['Info']['Birth'][5:7]

# season을 구하는 코드를 작성하세요: your code here
if 3<=int(b_month)<=5:
    season='Spring'
elif 6<=int(b_month)<=8:
    season='Summer'
elif 9<=int(b_month)<=11:
    season='Fall'
else:
    season='Winter'
print(f'{student_dict["Name"]}은 {student_dict["Major"]} 소속이며, 태어난 계절은 {season}, 키는 {float(height):.2f} 입니다. ')