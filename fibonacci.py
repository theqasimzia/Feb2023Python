def fibonacci(n):

    a = 0
    b = 1

    fib_seq = []

    for i in range(n):
        fib_seq.append(a)
        a, b = b, a+b
    return fib_seq

n = 10
fibnum = fibonacci(n)
print(fibnum)
