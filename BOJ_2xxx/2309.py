# 일곱 난쟁이

lst = []
for i in range(9):
    lst.append(int(input()))
sum_s = sum(lst)
num_1 = 0
num_2 = 0
for i in range(8):
    for j in range(i + 1, 9):
        if sum_s - (lst[i] + lst[j]) == 100:
            num_1 = lst[i]
            num_2 = lst[j]
lst.remove(num_1)
lst.remove(num_2)
lst.sort()
for i in lst:
    print(i)