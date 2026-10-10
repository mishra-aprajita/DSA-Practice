def g(n):
    if n == 0:
        return
    g(n - 1)
    print(n, end=" ")
    g(n - 1)


g(3)