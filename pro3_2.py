a=int(input())
b=list(map(int,input().split()[:a]))
c=list(reversed(sorted(b)))
print(c[0]+c[1])
