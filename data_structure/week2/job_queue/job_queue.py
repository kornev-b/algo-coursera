# python3

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
            next_worker = 0
            for j in range(self.num_workers):
                if next_free_time[j] < next_free_time[next_worker]:
                    next_worker = j
            self.assigned_workers[i] = next_worker
            self.start_times[i] = next_free_time[next_worker]
            next_free_time[next_worker] += self.jobs[i]

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()


# if __name__ == '__main__':
#     job_queue = JobQueue()
#     job_queue.solve()

def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def siftDown(a, i):
    while left_child(i) < len(a):
        min_i = i
        l = left_child(i)
        if (l < len(a) and (a[l][1] < a[min_i][1])) \
                or (l < len(a) and a[l][1] == a[min_i][1] and a[l][0] < a[min_i][0]
                    and a[min_i][1] + time[a[min_i][0]] == a[l][1] + time[a[l][0]]) \
                or (l < len(a) and a[min_i][1] + time[a[min_i][0]] > a[l][1] + time[a[l][0]]) \
                or (l < len(a) and counts[a[min_i][0]] > counts[a[l][0]]):
            min_i = l
        r = right_child(i)
        if (r < len(a) and (a[r][1] < a[min_i][1])) \
                or (r < len(a) and a[r][1] == a[min_i][1] and a[r][0] < a[min_i][0]
                    and a[min_i][1] + time[a[min_i][0]] == a[r][1] + time[a[r][0]]) \
                or (r < len(a) and a[min_i][1] + time[a[min_i][0]] > a[r][1] + time[a[r][0]]) \
                or (r < len(a) and counts[a[min_i][0]] > counts[a[r][0]]):
            min_i = r
        if i != min_i:
            a[i], a[min_i] = a[min_i], a[i]
            i = min_i
            continue
        break


def siftUp(a, i):
    while i > 0:
        p = parent(i)
        if (a[p][1] > a[i][1]):  # or (a[p][1] == a[i][1] and a[p][0] > a[i][0]):
            a[i], a[p] = a[p], a[i]
        i = p


def insert(a, k):
    a.append(k)
    siftUp(a, len(a) - 1)


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
    siftDown(a, 0)
    return max


with open('tests\\02') as f:
    content = f.read().splitlines()
num_workers, m = map(int, content[0].split())
jobs = map(int, content[1].split())

# num_workers, m = map(int, input().split())
# jobs = list(map(int, input().split()))

# num_workers = 4
# m = 20
tasks = []
# jobs = [10000,1000,1000,1000,1000]
# jobs = [1, 2, 3, 4, 5]
# jobs = [1, 1, 1, 1, 1]
# jobs = [1000000000, 1, 1, 1, 1, 1, 1, 1, 1]
# jobs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# jobs = [1, 1]
# jobs = [0, 0, 0, 0, 0, 0, 0, 0]
# jobs = [1, 2, 3]
a = []
time = []
counts = []
for i in range(0, num_workers):
    if i == len(jobs):
        break
    insert(a, (i, jobs[i]))
    tasks.append((i, 0))
    time.append(jobs[i])
    counts.append(0)
i = num_workers
while len(a) > 0:
    free = pop(a)
    t = time[free[0]]
    if i < len(jobs):
        insert(a, (free[0], free[1] + jobs[i]))
        tasks.append((free[0], t))
        time[free[0]] += jobs[i]
    i += 1
    counts[free[0]] += 1
for i in range(0, len(tasks)):
    print(i, tasks[i][0], tasks[i][1])

a = []
with open('tests\\02.a') as f:
    for line in f:
        int_list = [int(i) for i in line.split()]
        a.append(int_list)

for i in range(0, len(tasks)):
    assert tasks[i][0] == a[i][0] and tasks[i][1] == a[i][1], '{} {} != {} {}, index = {}'.format(tasks[i][0],
                                                                                                    tasks[i][1],
                                                                                                    a[i][0], a[i][1], i)
