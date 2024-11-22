string=input("enter a string")
word=string.lower().split()
a={}
for i in word:
        if i in a:
                a[i]=a[i]+1
        else:
             a[i]=1
for x,y in a.items():
        print(x,y)
