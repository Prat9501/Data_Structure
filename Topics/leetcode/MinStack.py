"""
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.minEl = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minEl) == 0 or x <= self.minEl[-1]:
            self.minEl.append(x)
        

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        else:
            if self.stack[-1] == self.minEl[-1]:
                self.minEl.pop()
            return self.stack.pop()
        

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minEl) == 0:
            return None
        else:
            return self.minEl[-1]

obj = MinStack()
obj.push(35)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()