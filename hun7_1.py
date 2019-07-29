a=int(input())
f=[]
b=list(map(int,input().split()[:a]))
c=list(map(int,input().split()))
d=b.index(c[0])
e=b.index(c[1])
if(d<e):
  for i in range(d,e):
    f.append(i)
  print(len(f))
else:
  for i in range(e,d):
    f.append(i)
  print(len(f))
