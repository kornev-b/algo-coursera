# Uses python3
import sys

import numpy as np


def fib_last_digit(n):
    a = [0] * (n + 1)
    a[0] = 0
    a[1] = 1
    for i in range(2, n + 1):
        a[i] = (a[i - 1] + a[i - 2]) % 10
    return a[n]


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


n = int(input())
print(fib_last_digit(n))
