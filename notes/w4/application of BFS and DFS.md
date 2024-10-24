# APPLICATION OF BFS AND DFS

BFS and DFS both systematically compute reachability of a vertex
### BFS:
* since bfs works level by level it can be used to compute shortest path
* 

### DFS:
* DFS explores a vertex as soon as it is visited 
* suspends a vertex while exploring its neighbours
* DFS numbering describes the order in which the vertices are explored


### Identifying connected components in a disconnected graph:
[[graphs#connected graphs:|connected graphs]] 
* we do this by assigning a component number to each vertex
* initialize component number of first vertex to 0
* start bfs or fds from vertex 0
    * all visited nodes form a connected component
    * assign each visited node component number 0
* then pick the smallest unvisited node j
    * increment component number to 1
    * run bfs or dfs from j
    * assign each visited node component number 0
* repeat until all vertices are visited

```python
def components(AList):
    component = {}
    for i in AList.keys():
        component[i] = -1

    (compid, seen) = (0, 0)

    while seen <= max(AList):
        startv = min([i for i in AList.keys() if component[i] = -1])
        visited = BFS(AList, startv)

        for i in visited.keys():
            if visited[i]:
                seen = seen + 1
                component[i] = compid
            compid = compid + 1

    return component
```

### finding cycles in a graph:
[[graphs#cyclic graphs:|cyclic graphs]]

