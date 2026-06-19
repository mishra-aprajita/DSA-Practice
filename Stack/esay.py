class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.stack:
            print("Underflow")
            return None
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            print("Underflow")
            return None
        return self.stack[-1] 

s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Top:", s.peek())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())   
