# BREADTH FIRST SEARCH
***

Explore the graph level by level
* first visit vertices of depth 1
* then 2 steps deep and so on

Each visited vertex has to be explored
* Extend the search to its neighbours
* Do this to each vertex one time only

Maintain information about vertices
* which vertices are visited
* which vertices are explored

Assume V = {0, 1, 2, ..., n-1}
* visited: V --> {True, False} tells us whether v in V has been visited or not
* Initially visited(v) = False for all v in V

Maintain a sequence of visited vertices yet to be explored
* lets use a queue and it will be initially empty

```python
class Queue:
    def __init__(self):
        self.queue = []

    def isempty(self):
        return self.queue == []

    def addq(self, v):
        self.queue.append(v):

    def delq(self):
        v = None
        if not self.isempty():
            v = self.queue[0]

        self.queue = self.queue[1:]

        return (v)
    def __str__(self):
        return (str(self.queue))

q = Queue()

for i in range(3):
    q.addq(i)
    print(q)

print q.isempty()

for i in range(3):
    print(q.delq(), q)

print q.isempty()
```
First add i to the queue

Then we remove and explore i (which is the starting point). If i not what we needed then
* for each edge(i, j), if visited(j) is False, set it to True
* add j to queue

Repeat the process
* stop when the queue is empty

```python

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

        for k in neighbours(Amat, j):
            if not visited[k]:
                visited[k] = True
                q.addq(k)
    return visited
```
