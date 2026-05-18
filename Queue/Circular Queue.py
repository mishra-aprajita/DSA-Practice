# Circular Queue using Array

size = 5
queue = [None] * size
front = rear = -1

# Add
def add(x):
    global front, rear

    if (rear + 1) % size == front:
        print("Full")

    else:
        if front == -1:
            front = 0

        rear = (rear + 1) % size
        queue[rear] = x


# First Element
def first():
    print(queue[front])


# Last Element
def last():
    print(queue[rear])


# Specific Location
def specific(i):
    print(queue[i])


# Function Calls
add(10)
add(20)
add(30)

first()
last()
specific(1)