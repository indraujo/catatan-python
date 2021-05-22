import collections
from collections import namedtuple

Point = namedtuple('Point','x y z')
newP = Point(3,4,5)
print(newP)

Point = namedtuple('Point','x qy zc h')
newP = Point(3,4,5,8)
print(newP)

Point = namedtuple('Point',['x','y','l'])
newP = Point(3,4,5)
print(newP)

Point = namedtuple('Point',{'x':1,'y':1,'l':1})
newP = Point(3,4,5)
print(newP)

Point = namedtuple('Point',{'x':1,'y':1,'l':1})
newP = Point(3,4,5)
print(newP.x,newP.y,newP.l)
print(newP._fields)

newP = newP._replace(x=6)
print(newP)

p2 = Point._make(['a','b','c'])
print (p2)