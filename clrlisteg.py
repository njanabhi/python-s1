#read 2 set of colours from the user and print out all the clr from 1st list not contained in list 2

i=input("enter colours in set1")

j=input("enter colours in set2")
m=i.split()
n=j.split()
diff=set(m).difference(set(n))
print(diff)