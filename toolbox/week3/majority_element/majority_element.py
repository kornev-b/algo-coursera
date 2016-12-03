# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return 0
    if left + 1 == right:
        return 1
    counter = 1
    maj_index = 0
    for i in range(1, len(a)):
        if a[i] == a[maj_index]:
            counter += 1
        else:
            counter -= 1
        if counter == 0:
            maj_index, counter = i, 1
    counter = 0
    for i in range(0, len(a)):
        if a[i] == a[maj_index]:
            counter += 1
    if counter > len(a) / 2:
        return 1
    return 0


input = sys.stdin.read()
n, *a = list(map(int, input.split()))
print(get_majority_element(a, 0, n))
# a = [512766168, 717383758, 5, 126144732, 5, 573799007, 5, 5, 5, 405079772]
# print(get_majority_element(a, 0, len(a)))
