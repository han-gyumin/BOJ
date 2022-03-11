# 저항
black = [0, 1]
brown = [1, 10]
red = [2, 100]
orange = [3, 1000]
yellow = [4, 10000]
green = [5, 100000]
blue = [6, 1000000]
violet = [7, 10000000]
grey = [8, 100000000]
white = [9, 1000000000]
data = {
    "black": black,
    "brown": brown,
    "red": red,
    "orange": orange,
    "yellow": yellow,
    "green": green,
    "blue": blue,
    "violet": violet,
    "grey": grey,
    "white": white,
}
first = data[input()]
second = data[input()]
third = data[input()]
print(int(str(first[0]) + str(second[0])) * int(third[1]))
