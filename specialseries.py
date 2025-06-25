def fib(n):
    a, b = 1, 1  # Start with first two Fibonacci numbers
    if n == 1 or n == 2:
        return 1
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return b

def prime(n):
    count = 0
    num = 2
    while True:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
            if count == n:
                return num
        num += 1

n = int(input())

if n % 2 == 0:
    print(prime(n // 2))
else:
    print(fib(n // 2 + 1))
