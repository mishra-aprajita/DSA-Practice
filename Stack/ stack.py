class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)
        print(item,"append")  

    def pop(self):
        if len(self.stack)==0:
            print("stack underflow")      
        else:
            (self.stack.pop(),"element popped")    

    def peek(self):
        if len(self.stack)==0:
            print("Stack is empty")
        else:
            print(self.stack[0])     

    def isEmpty(self):
        if len(self.stack)==0:
            print("stack is empty")
        else:
            print("stack is full")                   

    def display(self):
        print(self.stack)  

          


s = Stack()
s.push(10)       
s.push(20)       
s.push(30)  

s.pop()

s.display()