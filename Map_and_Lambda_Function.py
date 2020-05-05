cube = lambda x: x**3

def fibonacci(n):

    # Returns list of the first n Fibonacci sequence elements

    fib = []
    if n == 1:
        fib.append(0)
    elif n == 2:
        fib.append(0)
        fib.append(1)
    elif n >= 3:
        fib.append(0)
        fib.append(1)
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
    return fib


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
