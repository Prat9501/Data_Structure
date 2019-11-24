"""Consider the following SpecialStack
16  --> TOP
15
29
19
18

When getMin() is called it should return 15, which is the minimum
element in the current stack.

If we do pop two times on stack, the stack becomes
29  --> TOP
19
18

When getMin() is called, it should return 18 which is the minimum
in the current stack.
"""
class Queue():
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, x):
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(x)
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def deQueue(self):
        if len(self.s1) == 0:
            print('Queue is empty')
        x = self.s1[-1]
        self.s1.pop()

    def getmin(self):
        return min(self.s1)


if __name__ == '__main__':
    q = Queue()
    q.enQueue(18)
    q.deQueue()
    q.enQueue(19)
    q.enQueue(29)
    print(q.getmin()) # 19
    q.enQueue(15)
    q.enQueue(16)
    print(q.getmin()) # 15
