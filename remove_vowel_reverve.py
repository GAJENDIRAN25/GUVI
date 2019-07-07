x=['a','e','i','o','u','A','E','I','O','U']
l=[]
a=input()
for i in a:
  if i in x:
    continue
  else:
    l.append(i)
for i in l[::-1]:
  print(i, end='')
  
