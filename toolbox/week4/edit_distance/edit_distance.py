# Uses python3
def edit_distance(first, second):
    n = len(first) + 1
    m = len(second) + 1
    d = [[0] * m for i in range(n)]
    for i in range(n):
        d[i][00] = i
    for i in range(m):
        d[0][i] = i
    for i in range(1, n):
        for j in range(1, m):
            insertion = d[i][j - 1] + 1
            deletion = d[i - 1][j] + 1
            match = d[i - 1][j - 1]
            mismatch = d[i - 1][j - 1] + 1

            if first[i - 1] == second[j - 1]:
                d[i][j] = min(insertion, deletion, match)
            else:
                d[i][j] = min(insertion, deletion, mismatch)
    # print_matrix(d)
    return d[n - 1][m - 1]


def print_matrix(a):
    for i in range(len(a)):
        print(a[i])


# first = "short"
# second = "ports"
# print(edit_distance(first, second))
print(edit_distance(input(), input()))
