# Uses python3
import sys


def optimal(W, weights):
    value = [[0] * (len(weights) + 1) for i in range(W + 1)]
    for i in range(1, len(weights) + 1):
        for w in range(1, (W + 1)):
            value[w][i] = value[w][i - 1]
            if weights[i - 1] > w:
                continue
            val = value[w - weights[i - 1]][i - 1] + weights[i - 1]
            if value[w][i] < val:
                value[w][i] = val
    # print(value)
    return value[W][n]


def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result


input = sys.stdin.read()
W, n, *w = list(map(int, input.split()))
# n = 3
# w = [1, 4, 8]
# W = 10
print(optimal(W, w))
