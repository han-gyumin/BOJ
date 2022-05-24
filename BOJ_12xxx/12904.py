# A와 B
s=input()
t=input()
while(True):
    if len(t)==len(s):
        break
    elif t[-1]=='A':
        t=t[:-1]
    elif t[-1]=='B':
        t=t[:-1]
        t=t[::-1]
if t==s:
    print(1)
else:
    print(0)