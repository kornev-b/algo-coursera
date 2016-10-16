# Uses python3
import sys


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
        if a[i] == 1 and a[i - 1] == 0:
            return a[:-2], i - 1
        i += 1


def partial_sum_last_digit(m, n):
    if n <= 1:
        return n
    a, p = pisano(n, 10)
    if len(a) == 0:
        return p
    rem = n % p
    div = n // p
    if div == 0:
        div = 1
    return int(((sum(a) * div) + sum(a[:rem + 1]) - sum(a[:m % p])) % 10)


def fibonacci_partial_sum_naive(from_, to):
    if to <= 1:
        return to

    previous = 0
    current = 1

    for _ in range(from_ - 1):
        previous, current = current, previous + current

    sum = current

    for _ in range(to - from_):
        previous, current = current, previous + current
        sum += current

    return sum % 10


while True:
    m, n = map(int, input().split())
    print(partial_sum_last_digit(m, n))
