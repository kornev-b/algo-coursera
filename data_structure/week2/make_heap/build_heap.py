# python3

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def GenerateSwaps(self):
        # TODO: replace by a more efficient implementation
        for i in range(len(self._data)):
            for j in range(i + 1, len(self._data)):
                if self._data[i] > self._data[j]:
                    self._swaps.append((i, j))
                    self._data[i], self._data[j] = self._data[j], self._data[i]

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()


swaps = []


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
        if l < len(a) and a[l] < a[min_i]:
            min_i = l
        r = right_child(i)
        if r < len(a) and a[r] < a[min_i]:
            min_i = r
        if i != min_i:
            a[i], a[min_i] = a[min_i], a[i]
            swaps.append((i, min_i))
            i = min_i
            continue
        break


def siftUp(a, i):
    while i > 0:
        p = parent(i)
        if a[parent(i)] > a[i]:
            a[i], a[p] = a[p], a[i]
            swaps.append((i, p))
        i = p


def buildHeap(a):
    for i in range(len(a) // 2, -1, -1):
        siftDown(a, i)
    return a


n = int(input())
data = [int(s) for s in input().split()]
# a = buildHeap([11, 2, 4, 5, 2, 18, 7, 5, 9, 9, 9])
# a = buildHeap([5, 4, 3, 2, 1])
# a = buildHeap([1, 2, 3, 4, 5])
# print(a)
# print(swaps)
buildHeap(data)
print(len(swaps))
for swap in swaps:
    print(swap[0], swap[1])
