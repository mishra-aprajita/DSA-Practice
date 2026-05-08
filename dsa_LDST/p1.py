# =========================
# Dynamic Array
# =========================
class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, x):
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = x
        self.size += 1
        print(f"Appended {x} | Size: {self.size}, Capacity: {self.capacity}")

    def resize(self):
        print("Resizing...")
        self.capacity *= 2
        new_arr = [None] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr

    def pop(self):
        if self.size == 0:
            print("Array is empty")
            return None

        val = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        print(f"Popped {val} | Size: {self.size}")
        return val

    def print_array(self):
        print("Array:", [self.arr[i] for i in range(self.size)])


# =========================
# Singly Linked List
# =========================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_by_value(self, x):
        temp = self.head

        if temp and temp.data == x:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != x:
            prev = temp
            temp = temp.next

        if not temp:
            print("Value not found")
            return

        prev.next = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# =========================
# Doubly Linked List
# =========================
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, x):
        new_node = DNode(x)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def insert_after(self, target, x):
        temp = self.head
        while temp and temp.data != target:
            temp = temp.next

        if not temp:
            print("Target not found")
            return

        new_node = DNode(x)
        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    def delete_at_position(self, pos):
        if not self.head:
            return

        temp = self.head

        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        for _ in range(pos):
            temp = temp.next
            if not temp:
                return

        if temp.next:
            temp.next.prev = temp.prev

        if temp.prev:
            temp.prev.next = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


# =========================
# Stack (Using SLL)
# =========================
class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.head:
            print("Stack Underflow")
            return None

        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        if not self.head:
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None


# =========================
# Queue (Using SLL)
# =========================
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new_node = Node(x)
        if not self.tail:
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            print("Queue Underflow")
            return None

        val = self.head.data
        self.head = self.head.next

        if not self.head:
            self.tail = None

        return val

    def front(self):
        if not self.head:
            return None
        return self.head.data


# =========================
# Balanced Parentheses
# =========================
def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            stack.push(ch)
        elif ch in ")}]":
            if stack.is_empty():
                return False
            if stack.pop() != pairs[ch]:
                return False

    return stack.is_empty()


# =========================
# MAIN FUNCTION (TEST CASES)
# =========================
if __name__ == "__main__":

    print("\n--- Dynamic Array ---")
    da = DynamicArray()
    for i in range(10):
        da.append(i)

    da.print_array()
    da.pop()
    da.pop()
    da.pop()
    da.print_array()

    print("\n--- Singly Linked List ---")
    sll = SinglyLinkedList()
    sll.insert_at_beginning(3)
    sll.insert_at_beginning(2)
    sll.insert_at_beginning(1)

    sll.insert_at_end(4)
    sll.insert_at_end(5)
    sll.insert_at_end(6)

    sll.traverse()
    sll.delete_by_value(3)
    sll.traverse()

    print("\n--- Doubly Linked List ---")
    dll = DoublyLinkedList()
    for i in range(1, 6):
        dll.insert_end(i)

    dll.traverse()
    dll.insert_after(3, 99)
    dll.traverse()
    dll.delete_at_position(1)
    dll.traverse()

    print("\n--- Stack ---")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Pop:", stack.pop())
    print("Peek:", stack.peek())

    print("\n--- Queue ---")
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Dequeue:", queue.dequeue())
    print("Front:", queue.front())

    print("\n--- Parentheses Checker ---")
    tests = ["([])", "([)]", "(((", ""]
    for t in tests:
        print(f"{t} ->", "Balanced" if is_balanced(t) else "Not Balanced")