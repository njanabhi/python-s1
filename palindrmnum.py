n=int(input("enter a number"))
temp=n
a=0
while(n>0):
    d=n%10
    a=a*10+d
    n=n//10
if(temp==a):
        print("the number is palindrome")
else:
        print("number is not palindrome")