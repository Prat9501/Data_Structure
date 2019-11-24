class Queue():
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, x):
        """ takes O(n) """
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(x)
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def deQueue(self):
        """ takes O(1) """
        if len(self.s1) == 0:
            print('Queue is empty')
        x = self.s1[-1]
        self.s1.pop()
        return x

if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
    print(q.deQueue())
    print(q.deQueue())

"""
s1 = [], s2 =[]
q.enQueue(1) --> go to line 10 --> s1 = [1]
q.enQueue(2) --> go to line 7 --> s2 = [1], s1 = [] --> s1 = [2] --> s1 = [2,1], s2 =[]
q.enQueue(3) --> go to line 7 --> s2 = [2,1], s1 =[] --> s1 = [3] --> s1 = [3,2,1], s2 = []

q.deQueue() --> s1 = [3,2,1] go to line 18 --> x = 1
q.deQueue() --> s1 = [3,2] go to line 18 --> x = 2
"""
