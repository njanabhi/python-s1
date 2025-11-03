class Student:
    def getdata(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def displayStudent(self):
        print("Roll No:",self.rollno)
        print("Name:",self.name)
        print("course:",self.course)
class Test(Student):
    def getmarks(self,marks):
        self.marks=marks
    def displaymarks(self):
        print("Total marks:",self.marks)
        
r=int(input("Enter the roll no:"))
n=str(input("Enter the name:"))
c=str(input("Enter the course:"))
m=int(input("Enter the marks:"))
print ("Result") 
student=Test() 
student.getdata(r,n,c) 
student.getmarks(m) 
student.displayStudent() 
student.displaymarks()

    