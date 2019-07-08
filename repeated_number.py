from collections import Counter
li=[]
a=int(input())
b=list(map(int,input().split()))
c=Counter(b)
for i,j in c.items():
  if(j>1):
    li.append(i)
if(len(li)==0):
  print('unique')
else:
  for i in li:
    print(i, end=' ')
