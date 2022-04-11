# 문제 1
print("문제 1")
text = "the quick brown fox jumps over the lazy dog"
### code here ###

words = text.split()

cased_words = [i[0].upper() + i[1:] for i in words]

output = " ".join(cased_words)

### code here ###
print(output)

print()
print()

print("문제 2")
text = "1.jpg,10.png,11.png,2.jpg,3.png"
files = text.split(",")
### code here ###


def formatting(x):
    tmpRet = [file.split(".") for file in files]
    ret = [f"{int(tmp[0]):05d}.{tmp[1]}" for tmp in tmpRet]
    return ret


ret = formatting(files)
### code here ###

print(ret)
print()
print()

print("문제 3-1")
melon_chart = [
    [1, "TOMBOY", "(여자)아이들"],
    [2, "GANADARA (Feat. 아이유)", "박재범"],
    [3, "Feel My Rhythm", "Red Velvet (레드벨벳)"],
    [4, "사랑은 늘 도망가", "임영웅"],
    [5, "사랑인가봐", "멜로망스"],
]

melon_chart_dictionary = {}
for i, j, k in melon_chart:
    melon_chart_dictionary[i] = [j, k]

### code here ###

print(melon_chart_dictionary)

print()
print()

print("문제 3-2")
### code here ###

for key, item in melon_chart_dictionary.items():
    print(f"{key}위: {item[0]} | {item[1]}")

### code here ###

print()
print()

print("문제 3-3")
### code here ###

for key, value in melon_chart_dictionary.items():
    if key == 1:
        tmpValue = melon_chart_dictionary[key]
    if key == 2:
        melon_chart_dictionary[1] = value
        melon_chart_dictionary[2] = tmpValue

for key, item in melon_chart_dictionary.items():
    print(f"{key}위: {item[0]} | {item[1]}")

### code here ###
