a=input()
count=0
for i in a:
  if(i.isnumeric()==True):
    count+=1
  else:
    continue
print(count)
