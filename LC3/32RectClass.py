class rectangle:
    def __init__(self,l1,b1):
        self.l=l1
        self.b=b1
    def area(self):
        return(self.l*self.b)
    def peri(self):
        print("IT'S PERIMETER : ",(2*(self.l+self.b)))
    def compare(self,obj):
        if(self.area()==obj.area()):
            print("EQUAL")
        else:
            print("NOT EQUAL")
x1 = rectangle(6, 4)
a=x1.area()
print("AREA RECTANGLE 1 : ",a)
x1.peri()
x2 = rectangle(4, 4)
b=x2.area()
print("AREA RECTANGLE 2 : ",b)
x2.peri()
x1.compare(x2)
