class MyCircularQueue:

    def __init__(self, k):
        self.head = -1
        self.tail = -1
        self.size = k
        self.data = [None for i in range(k)]
        
        

    def enQueue(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.data[self.tail] = value
        return True
        

    def deQueue(self):
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return True
        self.head = (self.head + 1) % self.size
        return True
       

    def Front(self):
        if self.isEmpty():
            return -1
        return self.data[self.head]
        

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.data[self.tail]
        

    def isEmpty(self):
        return self.head == -1

    def isFull(self):
        return ((self.tail + 1) % self.size) == self.head


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)
param_1 = obj.enQueue(8)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()

print(obj.data)