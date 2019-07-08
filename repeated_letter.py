from collections import Counter
a=list(map(str,input()))
b=Counter(a)
c=max(b.values())
for i in b.items():
  if(i[1]==c):
    print(i[0])
  
