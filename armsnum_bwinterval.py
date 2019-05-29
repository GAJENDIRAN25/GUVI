x,y=input().split()
a=int(x)
b=int(y)
for i in range(a+1,b):
sum=0
temp=i
  while(i!=0):
    i=i%10
    sum+=i*i*i
    i=i//10
    if(temp==sum):
      print(sum, end=' ')
