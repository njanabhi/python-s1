s1={1,2,3}
s2={1,2,3,'abcd'}
print(s1)
print(s2)

s3=s1.union(s2)
print(s3)
s4=s1.intersection(s2)
print(s4)
s5=s1.difference(s2)
print(s5)
s6=s2.difference(s1)
print(s6)