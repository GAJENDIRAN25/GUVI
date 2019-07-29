a=int(input())
b=list(map(int,input().split()[:a]))
for i in range(len(b)-1):
  if(b[i]>b[i+1]):
    print(b[i],end=' ')
  else:
    print(b[i+1],end=' ')
