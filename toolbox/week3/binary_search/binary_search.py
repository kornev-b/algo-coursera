# Uses python3
import sys


def binary_search(a, x):
    left, right = 0, len(a)
    if right == 1:
        if a[left] == x:
            return left
        return -1
    while left <= right:
        center = (left + right) // 2
        if center >= len(a) or center < 0:
            return -1
        if a[center] == x:
            return center
        elif x < a[center]:
            right = center - 1
            continue
        left = center + 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


input = sys.stdin.read()
data = list(map(int, input.split()))
n = data[0]
m = data[n + 1]
a = data[1: n + 1]
for x in data[n + 2:]:
    print(binary_search(a, x), end=' ')
# a = [5, 1, 5, 8, 12, 13]
# data = [8, 1, 23, 1, 11]
# for x in data:
#     print(binary_search(a, x), end=' ')
