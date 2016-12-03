# Uses python3
import sys
import numpy as np

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    sorted = [0] * len(weights)
    for i in range(0, len(weights)):
        sorted[i] = values[i] / weights[i]
    a_sorted = np.array(sorted).argsort()[::-1][:n]
    for i in range(0, len(weights)):
        if capacity == 0:
            return value
        a = min(weights[a_sorted[i]], capacity)
        value += a * sorted[a_sorted[i]]
        capacity -= a
    return value


data = list(map(int, sys.stdin.read().split()))
n, capacity = data[0:2]
values = data[2:(2 * n + 2):2]
weights = data[3:(2 * n + 2):2]
# n, capacity = 1, 10
# values = [500]
# weights = [30]
opt_value = get_optimal_value(capacity, weights, values)
print("{:.10f}".format(opt_value))
