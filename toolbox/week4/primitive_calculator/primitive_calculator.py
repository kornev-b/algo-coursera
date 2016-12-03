# Uses python3

SUM_1 = 0
MULT_2 = 1
MULT_3 = 2


def optimal(n):
    if n == 1:
        return [1]
    digits = [0] * n
    indexes = [0] * n
    costs = [0] * n
    digits[0] = 1

    for i in range(1, n):
        digit = i + 1
        digits[i] = digit
        if digit % 3 == 0:
            index = digit // 3 - 1
        elif digit % 2 == 0:
            index = digit // 2 - 1
        else:
            index = i - 1
        if costs[index] + 1 > costs[i - 1] + 1:
            indexes[i] = i - 1
            costs[i] = costs[i - 1] + 1
            continue
        indexes[i] = index
        costs[i] = costs[index] + 1

    result = [n]
    index = indexes[n - 1]

    for i in range(n - 1, 0, -1):
        if result[len(result) - 1] == 1:
            break
        result.append(digits[index])
        index = indexes[index]
    result.reverse()
    return result


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


# while True:
n = int(input())
seq = optimal(n)
print(len(seq) - 1)
for x in seq:
    print(x, end=' ')
