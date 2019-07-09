a,b=map(int,input().split())
li=[]
c=list(map(int,input().split()))
d=list(map(int,input().split()))
for i in c:
  for j in d:
    if i == j:
      li.append(i)
if(len(c)==len(d)):
  if(li==c):
    print('YES')
  else:
    print('NO')
elif(len(li)==0):
  print('NO')
else:
  print('YES')
