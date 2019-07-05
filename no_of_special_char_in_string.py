a=input()
count=0
for i in a:
  if(i.isalpha()==True or i.isnumeric()==True or i==' ' ):
    continue
  else:
    count+=1
print(count)
