# Uses python3


def pisano(n, m):
    if n == 0:
        return [], 0
    elif n == 1:
        return [], 1
    i = 2
    a = [0] * (6 * m + 2)
    a[0] = 0
    a[1] = 1
    while i < len(a):
        a[i] = (a[i - 2] + a[i - 1]) % m
        if i == n:
            return a[:i + 1], i
        if a[i] == 1 and a[i - 1] == 0:
            return a[:-2], i - 1
        i += 1


def sum_last_digit(n):
    a, p = pisano(n, 10)
    if len(a) == 0:
        return p
    rem = n % p
    div = n // p
    if div == 0:
        div = 1

    return int(((sum(a) * div) + sum(a[:rem + 1])) % 10)


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


while True:
    n = int(input())
    print(sum_last_digit(n))
