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
        if (l < len(a) and (a[l][1] < a[min_i][1])) or (
                        a[l][1] == a[min_i][1] and a[l][0] < a[min_i][0]):
            min_i = l
        r = right_child(i)
        if (r < len(a) and (a[r][1] < a[min_i][1])) or (
                            r < len(a) and a[r][1] == a[min_i][1] and a[r][0] < a[min_i][0]):
            min_i = r
        if i != min_i:
            a[i], a[min_i] = a[min_i], a[i]
            i = min_i
            continue
        break


def siftUp(a, i):
    while i > 0:
        p = parent(i)
        if (a[p][1] > a[i][1]) or (a[p][0] == a[i][0] and a[p][1] > a[i][1]):
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


# num_workers, m = map(int, input().split())
# jobs = list(map(int, input().split()))

num_workers = 4
# m = 20
tasks = []
# jobs = [10000,1000,1000,1000,1000]
# jobs = [1, 2, 3, 4, 5]
# jobs = [1, 1, 1, 1, 1]
# jobs = [1000000000, 1, 1, 1, 1, 1, 1, 1, 1]
jobs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# jobs = [1, 1]
a = []
time = []
for i in range(0, num_workers):
    if i == len(jobs):
        break
    insert(a, (i, jobs[i]))
    time.append(0)
i = num_workers
while len(a) > 0:
    free = pop(a)
    tasks.append((free[0], time[free[0]]))
    if i < len(jobs):
        insert(a, (free[0], jobs[i]))
    time[free[0]] += free[1]
    i += 1
for i in range(0, len(tasks)):
    print(tasks[i][0], tasks[i][1])
