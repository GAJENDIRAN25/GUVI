x=['a','e','i','o','u','A','E','I','O','U']
l=[]
lenth=int(input())
a=input()
if(lenth<=len(a)):
  for i in a:
    if i in x:
      continue
    else:
      l.append(i)
for i in l[::-1]:
  print(i, end='')
  
