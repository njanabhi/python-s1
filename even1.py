#pg to remove even numbers
n=list(map(int,input("enter your numbers:").split(',')))
list2=[]
for i in n:
    if int(i) % 2==0: continue
    list2.append(i)
print(list2)