def arithmetic(N,A,D):
   result= ((N/2)*(2*A+(N-1)*D))
   return result
a,b,c=input().split()
x=int(a)
y=int(b)
z=int(c)
print(int(arithmetic(x,y,z)))
