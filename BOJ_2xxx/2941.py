# 크로아티아 알파벳
a = input()
cnt = 0 
arr=["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in arr:
    a = a.replace(i,"1")
print(len(a))
