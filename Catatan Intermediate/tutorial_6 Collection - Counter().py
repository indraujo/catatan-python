#6 Collections
import collections
from collections import Counter

# Containers
# list
# set
# dict
# tuple - inmuttable

# types
# 1 Counter
# 2 deque
# 3 namedTuple()
# 4 orerDict
# 5 defaultdict

c = Counter("gallad")
print(c)
b = Counter(['a','a','b','c','c'])
print(c)
c = Counter({"a":1,"b":2})
print(c)
c = Counter(cats=4,dogs=7)

print(list(c.elements()))

print(b.most_common(2))

c = Counter(a=4,b=2,c=0,d=-2)
d = ['a','b','b','c','d']
c.subtract(d)
print(c)

c.update(d)
print(c)

c.clear()
print(c)

c = Counter(a=4,b=2,c=0,d=-2)
d = Counter(['a','b','b','c','d'])
print(c+d)