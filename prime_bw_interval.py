x,y=input().split()
a=int(x)
b=int(y)
for i in range(a+1,b):
    if(i>1):
        for j in range(2,i//2 + 1):
            if(i%j==0):
                break
        else:
            print(i,end=' ')
    else:
        break
    
