import numpy as np

# for the airlines graph
edges = [(0, 1), (0, 4),
         (1, 2), (2, 0),
         (3, 4), (3, 6),
         (4, 0), (4, 3), (4, 7),
         (5, 3), (5, 7),
         (6, 5),
         (7, 4), (7, 8),
         (8, 5), (8, 9),
         (9, 8)]


A = np.zeros(shape=(10, 10))

for (i, j) in edges:
    A[i, j] = 1



AList = {}

for i in range(10): # since there are 10 vertices in G
    AList[i] = []

for (i, j) in edges:
    AList[i].append(j)

# print(AList)

# output = {0: [1, 4], 1: [2], 2: [0], 3: [4, 6], 4: [0, 3, 7], 5: [3, 7], 6: [5], 7: [4, 8], 8: [5, 9], 9: [8]}


def neighbours(AMat, i):

    nbrs = []

    (rows, cols) = AMat.shape

    for j in range(cols):

        if AMat[i,j] == 1:

            nbrs.append(j)

    return(nbrs)

#print(neighbours(A,7))

class Queue:
    def __init__(self):
        self.queue = []

    def isempty(self):
        return self.queue == []

    def addq(self, v):
        self.queue.append(v)

    def delq(self):
        v = None
        if not self.isempty():
            v = self.queue[0]

        self.queue = self.queue[1:]

        return (v)
    def __str__(self):
        return (str(self.queue))

q = Queue()
'''
for i in range(3):
    q.addq(i)
    print(q)

print (q.isempty())

for i in range(3):
    print(q.delq(), q)

print (q.isempty())
'''

def BFS(AMat, v):
    (rows, columns) = AMat.shape
    visited = {}

    for i in range(rows):
        visited[i] = False # setting visited false for all vertices

    q = Queue()

    visited[v] = True # setting visited True for the first vertex
    q.addq(v)

    while q.isempty():
        j = q.delq()

        for k in neighbours(AMat, j):
            if not visited[k]:
                visited[k] = True
                q.addq(k)
    return visited

