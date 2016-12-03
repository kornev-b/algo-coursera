# Uses python3
import sys
import math
import numpy as np

"""
Distributive property of modulo:
(x + y) % n = (x % n) + (y % n)
"""


def pisano(n, m):
    if m == 0:
        return 0
    elif m == 1:
        return n
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    # if is_power_two(m) and n > m:
    #     return [], np.int64(3 * m / 2)
    # if is_power(m, 5) and n > m:
    #     return [], np.int64(4 * m)
    # if is_power(m / 2, 5) and n > m:
    #     return [], np.int64(6 * m)
    i = 2
    a = [0] * (6 * m + 2)
    a[0] = 0
    a[1] = 1
    while i < sys.maxsize:
        # a[i] = fib(i) % m
        a[i] = (a[i - 2] + a[i - 1]) % m
        if i == n:
            return [], a[i]
        if a[i] == 1 and a[i - 1] == 0:
            return a, i - 1
        i += 1


def fib(n):
    a = [0] * (n + 1)
    a[0] = int(0)
    a[1] = int(1)
    i = 2
    end = n + 1
    while i < end:
        a[i] = a[i - 1] + a[i - 2]
        i += 1
    return a[i - 1]


def is_power(x, y):
    temp = math.log(x, y)
    return temp == int(temp)


def is_power_two(n):
    return n & (n - 1) == 0


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


# while True:
n, m = map(int, input().split())
a, p = pisano(n, m)
if len(a) == 0:
    print(p)
else:
    print(a[n % p])
