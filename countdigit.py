a=int(input())
count=0
while(a!=0):
  last=a%10
  count+=1
  a=a//10
print(count)
