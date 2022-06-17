# 일곱 난쟁이

lst=[]
for i in range(9):
    lst.append(int(input()))
final=[]
lst.sort()
sum=0
for i in range(len(lst)):
    
    sum=0
    sum+=lst[i]
    final.append(lst[i])
    if sum==100:
        break
    for j in range(1,len(lst)):
        if sum==100:
            break
        sum+=lst[j]
        final.append(lst[j])
        for a in range(2,len(lst)):
            if sum==100:
                break
            sum+=lst[a]
            final.append(lst[a])
            for b in range(3,len(lst)):
                if sum==100:
                    break
                sum+=lst[b]
                final.append(lst[b])
                for c in range(4,len(lst)):
                    if sum==100:
                        break
                    sum+=lst[c]
                    final.append(lst[c])
                    for d in range(5,len(lst)):
                        if sum==100:
                            break
                        sum+=lst[d]
                        final.append(lst[d])
                        for e in range(6,len(lst)):
                            if sum==100:
                                break
                            sum+=lst[e]
                            final.append(lst[e])
                            for f in range(7,len(lst)):
                                if sum==100:
                                    break
                                sum+=lst[f]
                                final.append(lst[f])
                                for g in range(8,len(lst)):
                                    if sum==100:
                                        break
                                    sum+=lst[g]
                                    final.append(lst[g])
                                final=[]
for i in final:
    print(i)