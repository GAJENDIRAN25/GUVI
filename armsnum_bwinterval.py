x,y=input().split()
a=int(x)
b=int(y)
for i in range(a+1,b):
  temp=i
  sum=0
  while(i!=0):
    c=i%10
    sum=sum+c*c*c
    i=i//10
  if(temp==sum):
    print(sum, end=' ')
