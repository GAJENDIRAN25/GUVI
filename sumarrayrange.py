a,b=input().strip()
x=int(a)
y=int(b)
for i in range(1,x+1):
  print(i, end=' ')
  while(i<=y):
    sum+=i
  print(sum)
