final_year=int(input("enter the final year"))
for i in range(2023,final_year):
    if (i%4==0)or(i%400==0)and(i%100!=0):
      print("the leap years are",i)
