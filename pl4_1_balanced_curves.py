a=[]
l=int(input())
for i in range(0,l):
  i=input()
  a.append(i)
for i in a:
  if(i.count('(')==i.count(')')):
    print('yes')
  else: 
    print('no')
 
