n=int(input("enter a number"))
s=0
a=1
b=1
i=1
print("fibonacci is",n,":")
while i<n:
    print(a)
    s=a+b
    a=b
    b=s
    i+=1
