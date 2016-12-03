# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def min_and_max(M, m, i, j, op):
    mmin = 0
    mmax = 0
    for k in range(i, j - 1):
        a = evalt(M[i][k], M[k + 1][j], op[k])
        b = evalt(M[i][k], m[k + 1][j], op[k])
        c = evalt(m[i][k], M[k + 1][j], op[k])
        d = evalt(m[i][k], m[k + 1][j], op[k])
        mmin = min(a, b, c, d)
        mmax = max(a, b, c, d)
    return mmin, mmax


def parse(dataset):
    op = []
    digits = []
    for i in range(len(dataset)):
        if not (dataset[i].isdigit()):
            op.append(dataset[i])
            continue
        digits.append(int(dataset[i]))
    return op, digits


def get_maximum_value(dataset):
    op, digits = parse(dataset)
    M = [[0] * len(digits) for i in range(len(digits))]
    m = [[0] * len(digits) for i in range(len(digits))]

    for i in range(len(digits)):
        m[i][i] = digits[i]
        M[i][i] = digits[i]
    for s in range(1, len(digits) - 1):
        for i in range(1, len(digits) - s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(M, m, i, j, op)
    print_matrix(M)
    print('\n')
    print_matrix(m)
    return M[1][len(digits) - 1]


def print_matrix(a):
    for i in range(len(a)):
        print(a[i])


input = "5-8+7*4-8+9"
print(get_maximum_value(dataset=input))
