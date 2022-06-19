character={
    "name":'기사',
    'level':12,
    "items":{
        "sword":"불꽃의 검",
        "armor":"풀플레이트"
    },
    "skill":["베기","세게 베기","아주 세게 베기"]
}

# characte={"name":'기사','level':12,"items":{"sword":"불꽃의 검","armor":"풀플레이트"},"skill":["베기","세게 베기","아주 세게 베기"]}

# name : 기사
# level : 12
# sword : 불꽃의 검
# armor : 풀플레이트
# skill : 베기
# skill : 세게 베기
# skill : 아주 세게 베기

for i in character:
    if type(character[i])!=dict and type(character[i])!=list:
        print(f'{i} : {character[i]}')
    elif type(character[i])==list:
        for j in character[i]:
            print(f'{i} : {j}')
    elif type(character[i])==dict:
        for j in character[i]:
            print(f'{j} : {character[i][j]}')

# your code here
a=[]
def multiplication_table(num):
    for i in range(1,10):
        print(f'{num} x {i} = {num*i}')
        a.append(num*i)
    return a

a = multiplication_table(3)
print(a)