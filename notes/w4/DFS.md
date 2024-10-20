# DEPTH FIRST SEARCH

lets take the airplanes graph as an example
* in DFS we start from vertex i visit unexplored vertex j
* then we suspend exploration of i and explore j
* if j have unexplored neighbours then we suspend j and visit its neighbour
* repeat this process until no neighbours are available
* here we use a stack to store the vertices

Code for DFS using Adjacency matrix

```python

(visited, parent) = ({}, {})

def DFS_global_init(AMat, v):
    (rows, cols) = AMat.shape

    for i in range(rows):
        visited[i] = False
        parent[i] = -1
    return


def DFS(Amat, v):
    visited[v] = True

    for k in neigbours(Amat, v):
        if not visited[k]:
            parent[k] = v
            DFS(Amat, k)
    return

```

Code for DFS using adjacency list

```python

(visited, parent) = ({}, {})

def DFS_global_init(AList, v):
    for i AList.keys():
        visited[i] = False
        parent[i] = -1
    return


def DFS_List(AList, v):
    visited[v] = True

    for k in AList[v]:
        if not visited[k]:
            parent[k] = v
            DFS_List(AList, k)
    return

```

### Complexity of DFS:
Overall complexity is same as the BFS
* O(n<sub>2</sub>) for AMat
* O(m + n) for AList
