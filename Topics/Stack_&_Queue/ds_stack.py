from collections import deque
from queue import LifoQueue
stack = deque()
stack.append('a')
stack.append('b')
print(stack) #deque(['a', 'b'])
print(stack.pop()) #b
print(stack) #deque(['a'])
print("=======================")

new_stack = LifoQueue(maxsize=5)
print(new_stack.qsize()) #0
new_stack.put('p')
new_stack.put('r')
new_stack.put('a')
new_stack.put('t')
print(new_stack.full()) #False
print(new_stack.qsize()) #4
print(new_stack.get()) #t
