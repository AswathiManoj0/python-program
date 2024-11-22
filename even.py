even_number=[]
odd_number=[]
my_list=[1,2,3,4,5,6,7]
print("the list is",my_list)
for num in my_list:
  if num%2==0:
     even_number.append(num)
  else:
      odd_number.append(num)
print("the even numbers are",even_number)
print("the odd numbers are",odd_number)
