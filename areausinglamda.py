area1=lambda b,h:1/2*b*h
b=int(input("enter the breadth:"))
h=int(input("enter the height:"))
print("The area of triangle is:",area1(b,h))

area2=lambda a:a*a
a=int(input("enter the side:"))
print("The area of square is:",area2(a))

area3=lambda a,b:a*b
a=int(input("enter the length:"))
b=int(input("enter the breadth:"))
print("The area of rectangle is:",area3(a,b))