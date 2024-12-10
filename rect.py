class Rectangle:
    def __init__(self, length, breadth):
      
        self.length = length
        self.breadth = breadth

    def area(self):
     
        return self.length * self.breadth

    def perimeter(self):
        
        return 2 * (self.length + self.breadth)

    def compare_area(self, o):
        
        if self.area() > o.area():
            return "The first rectangle is larger."
        elif self.area() < o.area():
            return "The second rectangle is larger."
        else:
            return "Both rectangles have the same area."

rect1 = Rectangle(6, 7)
rect2 = Rectangle(5, 3)

print(f"Rectangle 1 Area: {rect1.area()}")         
print(f"Rectangle 1 Perimeter: {rect1.perimeter()}") 
print(f"Rectangle 2 Area: {rect2.area()}")      
print(f"Rectangle 2 Perimeter: {rect2.perimeter()}") 
print(rect1.compare_area(rect2))

    
