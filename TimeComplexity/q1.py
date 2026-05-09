n=10
s = 0
for i in range(n):
    for j in range(0, n, 3):
        s += 1
        print(s)
        



# O(1) Constant
print("Hello")

# O(n) Linear
n = 5
for i in range(n):
    print(i)

# O(n²) Quadratic
for i in range(n):
    for j in range(n):
        print(i, j)

# O(n³) Cubic
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)