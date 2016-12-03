# Uses python3
import numpy as np

def max_indexes(a):
    max1 = np.argmax(a)
    max2 = 0
    temp = 0
    for i in range(0, len(a)):
        if i != max1 and a[i] > temp:
            temp = a[i]
            max2 = i
    return max1, max2


n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

# result = 0

# for i in range(0, n):
#     for j in range(i+1, n):
#         if a[i]*a[j] > result:
#             result = a[i]*a[j]

max1, max2 = max_indexes(a)
print(a[max1] * a[max2])
