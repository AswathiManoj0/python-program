factor=[]
num=int(input("enter a number"))
for i in range(1,num+1):
        if num%i==0:
          factor.append(i)
print("the factors are",factor)
