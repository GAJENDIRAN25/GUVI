n1 = int(input())                  
for i in range(2**n1):
    b1 = bin(i)[2:]
    l = len(b1)
    b1 = str(0) * (n1 - l) + b1
    print (b1)
