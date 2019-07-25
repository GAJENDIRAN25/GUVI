x1,y1=map(str,input().split())
a=list(x1)
b=list(y1)
c1=zip(a,b)
c1=list(c1)
d = []
for i in c1:
  if(len(i) == i.count(i[0])):
    d.append(i[0])
e1 = len(b) - len(d)
print(e1)
