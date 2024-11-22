x=[1,3,4,2,5,6,17,28]
print("the greatest number is:",max(x))
c=max(x)
f='prime'
print("position:",(x.index(max(x))+1))
for i in range(2,c):
      if(c%i==0):
        f='not prime'
print(f)
