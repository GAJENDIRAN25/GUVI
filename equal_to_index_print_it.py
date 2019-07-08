a=int(input())
l=[]
b=list(map(int,input().split()))
for i in range(len(b)):
  if(i==b[i]):
    l.append(i)
if(len(l)>0):
  for i in l:
    print(i, end=' ')
else:
  print('-1')
