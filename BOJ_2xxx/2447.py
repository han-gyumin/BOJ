num=int(input())

def star(n):
    if n==3:
        print("***")
        print("* *")
        print("***")
    else:
        n*star(n/3)

star(num)