# set
s = set()
s.add('a')
s.add('b')
s.add('c')
s.add('a')
print(s)

s1 = {1,2,3,4}
s2 = {1,2}
s3 = {9}
print(s1.union(s3))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1 - s2)



