mem = dict()


def fib(n):
    global mem
    if n in mem:
        return mem[n]
    if n <= 1:
        return n
    else:
        mem[n] = fib(n - 1) + fib(n - 2)
    return mem[n]


def fib_iterative(n):
    global mem
    mem[0] = 0
    mem[1] = 0
    for i in range(2, n+1):
        mem[n] = fib(n - 1) + fib(n - 2)
    return mem[n]


print fib(10), fib_iterative(10)
