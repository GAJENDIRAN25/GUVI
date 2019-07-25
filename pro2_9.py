a=int(input())
b=[]
for i in range(a):
  i=list(map(int,input().split()))
  b.append(i)
c=[]
for i in b:
  c=c+i
for i in sorted(c):
  print(i, end=' ')
