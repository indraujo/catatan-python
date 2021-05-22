import collections
from collections import deque

d = deque("hello")
d.append('4')
d.appendleft(5)
print(d)


d = deque("hello")
d.pop()
d.popleft()
print(d)

d.clear()

d.extend('456')
d.extendleft([1,2,3])
d.extendleft('hey')
print(d)

d.rotate(-2)
print(d)

d = deque("hello",maxlen=5)
#d.maxlen = 5
print(d)
d.extend([1,2,3])
print(d)
