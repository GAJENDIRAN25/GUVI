a,b=map(int,input().split())
li=[]
c=list(map(int,input().split()))
d=list(map(int,input().split()))
for i in c:
  for j in d:
    if i == j:
      li.append(i)
if(c==li):
  print('NO')
elif(len(li)==0):
  print('NO')
else:
  print('YES')
