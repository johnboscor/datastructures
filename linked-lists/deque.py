# internal implementation of ll. It is a double ll.
from collections import deque
llist = deque([1,2,3,4])
print(llist)
llist.reverse()
print(llist)
llist.appendleft(5)
print(llist)
llist.