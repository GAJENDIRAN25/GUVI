from collections import Counter
a=int(input())
b=list(map(int,input().split()))
c=Counter(b)
for i,j in c.items():
  if(j==1):
    print(i)
