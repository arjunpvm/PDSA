# DEPTH FIRST SEARCH

lets take the airplanes graph as an example
* in DFS we start from vertex i visit unexplored vertex j
* then we suspend exploration of i and explore j
* if j have unexplored neighbours then we suspend j and visit its neighbour
* repeat this process until no neighbours are available
* here we use a stack to store the vertices

```python

s = Stack()

def DFS_init(AMat, v):
    (rows, cols) = AMat.shape
    (visited, parent) = ({},{})
    stack = []

    for i in range(rows):
        visited[i] = False
        parent[i] = -1

    visited[v] = True
    parent[v] = 0
    stack.append(v)

    return DFS(AMat, v)


def DFS(Amat, v):
    while not s.isempty():
        j = stack[-1]

        for k in neighbours(AMat, j):
            if not visited[k]:
                visited[k] = True
                parent[i] = parent[j] + 1





```
