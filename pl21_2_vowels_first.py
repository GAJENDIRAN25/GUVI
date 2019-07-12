a=input()
c=''
d=''
for i in a:
  if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
    c=c+i
  else:
    d=d+i
print(c+d)
