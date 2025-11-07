class Rectangle:
    def getdata(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def displayarea(self):
        print("Length:",self.length)
        print("Breadth:",self.breadth)
        print("Area:",self.length*self.breadth)
class Perimeter(Rectangle):
    def getdata(self,perimeter):
        self.perimeter=perimeter
    def displayperimeter(self):
        print("Perimeter:",2*(self.length + self.breadth))
l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
print("Result")
shape=Rectangle()
shape.getdata(l,b)
shape.displayarea()
shape.displayperimeter()





