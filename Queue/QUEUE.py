class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        if self.q:
            print("Deleted:", self.q.pop(0))
        else:
            print("Queue Empty")

    def first(self):
        print("First:", self.q[0])

    def last(self):
        print("Last:", self.q[-1])

    def display(self):
        print("Queue:", self.q)


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.first()
q.last()

q.dequeue()

q.display()