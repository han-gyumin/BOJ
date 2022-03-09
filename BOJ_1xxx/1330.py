#두 수 비교하기
a = []
a = list(map(int, input().split()))
if(a[0] > a[1]):
    print(">")
elif(a[0] < a[1]):
    print("<")
else:
    print("==")

