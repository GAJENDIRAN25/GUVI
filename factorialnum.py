a=int(input())
if(a==1):
    print(a)
else:
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    print(fact,end=' ')
