a=int(input())
b=list(map(int,input().split()))
c=sorted(b)
c.reverse()
d="".join(c)
print(int(d))
