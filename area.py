square_area= lambda a:a*a
x=int(input("enter size of square"))
print("area of square is",square_area(x))

rectangle_area=lambda l,b:l*b
a=int(input("enter the length of rectangle"))
b=int(input("enter the breadth of rectangle"))
print("area of rectangle is",rectangle_area(a,b))

triangle_area=lambda b,h:0.5*b*h
a=int(input("enter the breadth of triangle"))
b=int(input("enter the height of triangle"))
print("area of triangle is",triangle_area(a,b))
