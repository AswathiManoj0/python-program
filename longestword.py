a=input().split()
b=len(a[0])
c=a[0]
for i in a:
    if b<len(i):
        b=len(i)
        c=i
print("count:",b," "+"longest word",c)
