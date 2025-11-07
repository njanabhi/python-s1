class Rectangle:
    def getdata(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self,length,breadth):
        area=self.length*self.breadth
        print("The area is:",area)
    def perimeter(self,length,breadth):
        perimeter=2*(self.length+self.breadth)
        print("The perimeter is:",perimeter)
l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
print("Result:")
obj=Rectangle()
obj.getdata(l,b)
obj.area(l,b)
obj.perimeter(l,b)