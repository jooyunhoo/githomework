import sys

class Queue:
    def __init__(self):
        self.items = []
        self.max = max

    def size(self):
        return len(self.items)
    
    def isFull(self, max = 5):
        if self.size == max:
            return False
        else:
            return True

    def isEmpty(self):
        if self.size == 0:
            True
        else:
            False
    
    def enqueue(self, item):
        if self.isFull():
            print("Queue is full")
            
        self.items.insert(0,item)

    def dequeue(self):
        if self.isEmpty == True:
            print("None")
        
        self.items.pop()

    def printqueue(self):
        for items in self.items:
            print(items)

q = Queue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.printqueue()
print(q.size())
q.dequeue()
q.printqueue()
