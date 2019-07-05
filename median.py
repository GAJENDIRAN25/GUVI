from statistics import median
a=int(input())
b=list(map(int,input().split()))
c=sorted(b)
print(int(median(c)))
