x,y=input().split()
a=int(x)
b=int(y)
c=list(map(int,input().split()))
d=sorted(c)
e=d[::-1]
print(e[b-1])
