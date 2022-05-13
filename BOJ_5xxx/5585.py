# 거스름돈
coin=1000-int(input())
count=0
for i in range(6):
    count+=coin//500
    coin=coin%500
    count+=coin//100
    coin=coin%100
    count+=coin//50
    coin=coin%50
    count+=coin//10
    coin=coin%10
    count+=coin//5
    coin=coin%5
    count+=coin//1
    coin=coin%1
print(count)