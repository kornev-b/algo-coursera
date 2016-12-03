# python3

# import sys, threading
# sys.setrecursionlimit(10**7) # max depth of recursion
# threading.stack_size(2**27)  # new thread will get stack of such size
#
# class TreeHeight:
#         def read(self):
#                 self.n = int(sys.stdin.readline())
#                 self.parent = list(map(int, sys.stdin.readline().split()))
#
#         def compute_height(self):
#                 # Replace this code with a faster implementation
#                 maxHeight = 0
#                 for vertex in range(self.n):
#                         height = 0
#                         i = vertex
#                         while i != -1:
#                                 height += 1
#                                 i = self.parent[i]
#                         maxHeight = max(maxHeight, height)
#                 return maxHeight
#
# def main():
#   tree = TreeHeight()
#   tree.read()
#   print(tree.compute_height())
#
# threading.Thread(target=main).start()

import sys
from time import process_time


class Queue:
    def __init__(self):
        self.items = []
        self.first = 0

    def isEmpty(self):
        return self.first == len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def enqueue_list(self, a):
        self.items.extend(a)
        # # for x in a:
        # #     self.enqueue(x)
        # a.reverse()
        # a.extend(self.items)
        # self.items = a

    def dequeue(self):
        next = self.items[self.first]
        self.first += 1
        return next

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def last(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]


def height(n, tree):
    t = process_time()
    if n == 1:
        return 1
    verts = [None] * n
    for i in range(0, n):
        verts[i] = []
    root = 0
    for i in range(0, n):
        v = tree[i]
        if v == -1:
            root = i
            continue
        verts[tree[i]].append(i)
    for i in range(0, n):
        if len(verts[i]) == n - 1:
            return 2
    queue = Queue()
    queue.enqueue_list(verts[root])
    h = 1
    last = queue.last()
    while not (queue.isEmpty()):
        node = queue.dequeue()
        if node == last:
            h += 1
            queue.enqueue_list(verts[node])
            last = queue.last()
            continue
        queue.enqueue_list(verts[node])
    # print("elapsed time: ", process_time() - t)
    return h


n = int(sys.stdin.readline())
tree = list(map(int, sys.stdin.readline().split()))
# with open("tests\\22") as f:
#     content = f.readlines()
# n = int(content[0])
# tree = list(map(int, content[1].split()))
# n = 10
# tree = [8, 8, 5, 6, 7, 3, 1, 6, -1, 5]
print(height(n, tree))
