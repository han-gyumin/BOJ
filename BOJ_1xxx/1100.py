# 하얀 칸
a = []
for i in range(8):
    a.append(input())
count = 0
for i in range(0, 8):
    for j in range(0, 8):
        if (i + j) % 2 == 0 and a[i][j] == "F":
            count += 1

print(count)
