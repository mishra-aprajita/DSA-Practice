class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        print(self.q.pop(0))


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.q)

q.dequeue()

print(q.q)