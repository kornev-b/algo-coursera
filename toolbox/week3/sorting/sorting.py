# Uses python3
import sys
import random


def partition3(a, l, r):
    if len(a) == 1:
        return 0, 0
    x = a[l]
    m1 = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            m1 += 1
            a[i], a[m1] = a[m1], a[i]
    a[l], a[m1] = a[m1], a[l]
    m2 = m1
    for i in range(m2 + 1, r + 1):
        if a[i] == x:
            m2 += 1
            a[i], a[m2] = a[m2], a[i]

    return m1, m2


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)


input = sys.stdin.read()
n, *a = list(map(int, input.split()))
randomized_quick_sort(a, 0, n - 1)
for x in a:
    print(x, end=' ')
# a = [2, 3, 2, 5, 5, 4, 4, 4, 3]
# a = [2, 2]
# k = random.randint(0, len(a) - 1)
# k = 5
# print(k)
# a[0], a[k] = a[k], a[0]
# randomized_quick_sort(a, 0, len(a) - 1)
# for x in a:
#     print(x, end=' ')
