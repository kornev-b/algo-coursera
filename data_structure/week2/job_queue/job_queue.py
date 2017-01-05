# python3


def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def compareIfTime(a, first, second):
    # if counts[a[first][0]] < counts[a[second][0]]:
    #     return first
    # if counts[a[first][0]] > counts[a[second][0]]:
    #     return second
    if a[first][0] < a[second][0]:
        return first
    return second


def compare(a, first, second):
    if a[first][1] < a[second][1]:
        return first
    if a[first][1] > a[second][1]:
        return second
    return compareIfTime(a, first, second)


def choose_min(a, parent, left, right):
    if a[parent][1] == a[left][1] and a[parent][1] == a[right][1]:
        return compareIfTime(a, left, right)
    if a[parent][1] > a[left][1] and a[parent][1] > a[right][1]:
        return compare(a, left, right)
    candidate = compare(a, left, right)
    return compare(a, parent, candidate)


def sift_down(a, i):
    while left_child(i) < len(a):
        min_i = i
        l = left_child(i)
        r = right_child(i)
        min_i = choose_min(a, min_i, l, r)
        if i != min_i:
            a[i], a[min_i] = a[min_i], a[i]
            i = min_i
            continue
        break


def sift_up(a, i):
    while i > 0:
        p = parent(i)
        if a[p][1] > a[i][1]:  # or (a[p][1] == a[i][1] and a[p][0] > a[i][0]):
            a[i], a[p] = a[p], a[i]
        i = p


def insert(a, k):
    a.append(k)
    sift_up(a, len(a) - 1)


def pop(a):
    max = None
    if len(a) == 0:
        return max
    if len(a) == 1:
        return a.pop(0)
    # if a[len(a) - 1][1] == a[0][1]:
    #     return a.pop(0)
    a[0], a[len(a) - 1] = a[len(a) - 1], a[0]
    max = a.pop()
    sift_down(a, 0)
    return max


# with open('tests\\02') as f:
#     content = f.read().splitlines()
# num_workers, m = map(int, content[0].split())
# jobs = map(int, content[1].split())

num_workers, m = map(int, input().split())
jobs = list(map(int, input().split()))

# num_workers = 4
# m = 20
tasks = []
# jobs = [10000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
# jobs = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8]
# jobs = [1, 1, 1, 1, 1]
# jobs = [1000000000, 1, 1, 1, 1, 1, 1, 1, 1]
# jobs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# jobs = [1, 1]
# jobs = [0, 0, 0, 0, 0, 0, 0, 0]
a = []
counts = []
for i in range(0, num_workers):
    if i == len(jobs):
        break
    insert(a, (i, jobs[i]))
    tasks.append((i, 0))
    counts.append(0)
i = num_workers
while len(a) > 0:
    free = pop(a)
    t = free[1]
    if i < len(jobs):
        insert(a, (free[0], free[1] + jobs[i]))
        tasks.append((free[0], t))
    else:
        break
    i += 1
    counts[free[0]] += 1
for i in range(0, len(tasks)):
    print(tasks[i][0], tasks[i][1])

# a = []
# with open('tests\\02.a') as f:
#     for line in f:
#         int_list = [int(i) for i in line.split()]
#         a.append(int_list)
#
# for i in range(0, len(tasks)):
#     assert tasks[i][0] == a[i][0] and tasks[i][1] == a[i][1], '{} {} != {} {}, index = {}'.format(tasks[i][0], tasks[i][1], a[i][0], a[i][1], i)
