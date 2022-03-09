#명령 프롬프트
num = int(input())
result = []
for i in range(num):
    a = input()
    if i == 0:
        result = list(a)
        continue
    for j in range(len(result)):
        if result[j] != a[j]:
            result[j] = "?"

print("".join(result))
