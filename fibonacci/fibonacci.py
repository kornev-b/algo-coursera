# Uses python3
import numpy as np


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = [0] * (n + 1)
    a[0] = 0
    a[1] = 1
    for i in range(2, n + 1):
        a[i] = a[i - 1] + a[i - 2]
    return a[n]


def calc_fib_naive(n):
    if n <= 1:
        return n
    return calc_fib_naive(n - 1) + calc_fib_naive(n - 2)

while True:
    n = int(input())
    print(fib(n))
