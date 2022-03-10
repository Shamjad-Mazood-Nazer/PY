class Rectangle:
    def __init__(self, l, b):
        self._l1 = l
        self._b1 = b
    def area(self):
        area1 = self._l1 * self._b1
        return area1
    def __lt__(self, obj):
        if (self.area() < obj.area()):
            return "The area of Rectangle 1 is less than Rectangle 2"
        else:
            return "The area of Rectangle 2 is less than Rectangle 1"

print("RECTANGLE 1")
l = int(input("Enter the length of rectangle 1 : "))
b = int(input("Enter the breadth of rectangle 1 : "))
obj1 = Rectangle(l,b)
print("The area of Rectangle 1 is : ", obj1.area())

print("\nRECTANGLE 2")
l=int(input("Enter the length of rectangle 2 : "))
b=int(input("Enter the breadth of rectangle 2 : "))
obj2 = Rectangle(l,b)
print("The area of Rectangle 2 is : ", obj2.area())
print("\nNow Comparing The Rectangles")
print(obj1 < obj2)