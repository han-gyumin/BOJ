#덩치
num = int(input())
arr = []
for i in range(num):
    arr.append([])

for i in arr:
    a, b = map(int, input().split())
    i.append(a)
    i.append(b)
ranking = []
rank = 1
for i in range(num):
    for j in range(num):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank += 1
    ranking.append(rank)
    rank = 1
for i in ranking:
    print(i, end=" ")
