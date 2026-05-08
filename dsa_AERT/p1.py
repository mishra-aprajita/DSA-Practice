# AERT: Algorithmic Efficiency & Recursion Toolkit

# ---------------- STACK ADT ----------------
class StackADT:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# ---------------- FACTORIAL ----------------
def factorial(n):
    if n < 0:
        return "Invalid input"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# ---------------- FIBONACCI ----------------
call_count_naive = 0

def fib_naive(n):
    global call_count_naive
    call_count_naive += 1

    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)


call_count_memo = 0

def fib_memo(n, memo={}):
    global call_count_memo
    call_count_memo += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]


# ---------------- TOWER OF HANOI ----------------
def hanoi(n, source, auxiliary, destination, moves):
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        print(move)
        moves.push(move)
        return

    hanoi(n-1, source, destination, auxiliary, moves)

    move = f"Move disk {n} from {source} to {destination}"
    print(move)
    moves.push(move)

    hanoi(n-1, auxiliary, source, destination, moves)


# ---------------- BINARY SEARCH ----------------
def binary_search(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)


# ---------------- MAIN FUNCTION ----------------
if __name__ == "__main__":

    # Factorial Tests
    print("Factorial:")
    for n in [0, 1, 5, 10]:
        print(f"{n}! =", factorial(n))

    # Fibonacci Tests
    print("\nFibonacci:")
    for n in [5, 10, 20, 30]:
        call_count_naive = 0
        print(f"\nNaive fib({n}) =", fib_naive(n))
        print("Calls:", call_count_naive)

        call_count_memo = 0
        print(f"Memoized fib({n}) =", fib_memo(n))
        print("Calls:", call_count_memo)

    # Tower of Hanoi
    print("\nTower of Hanoi (N=3):")
    stack = StackADT()
    hanoi(3, 'A', 'B', 'C', stack)

    # Binary Search Tests
    print("\nBinary Search:")
    arr = [1, 3, 5, 7, 9, 11, 13]

    for key in [7, 1, 13, 2]:
        result = binary_search(arr, key, 0, len(arr)-1)
        print(f"Search {key}: Index =", result)

    # Empty array case
    print("Empty array test:", binary_search([], 5, 0, -1)) 