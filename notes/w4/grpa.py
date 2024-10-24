# GRPA 1

# Helper function
from collections import deque
class myQueue:
  def __init__(self):
    self.Q = deque()
  
  def deQueue(self):
    return self.Q.popleft()

  def enQueue(self, x):
    return self.Q.append(x)

  def isEmpty(self):
    return False if self.Q else True

def findConnectionLevel(n, Gmat, Px, Py):
  q = myQueue() 
  visited = [False for i in range(n)]
  q.enQueue(Px)
  q.enQueue(-1) #using -1 in queue to distinguish between levels in BFS.
  visited[Px]=True
  level=1;

  while not q.isEmpty():
    v = q.deQueue()
    if (v == -1):
      level+=1
      if (not q.isEmpty()):
        q.enQueue(-1)
      continue
    for i in range(n):
      if(i==Py and Gmat[v][i] == 1):
        return level
      if(Gmat[v][i] and (not visited[i])):
        q.enQueue(i)
        visited[i]=True

  return 0
vertices = int(input())
Amat = []
for i in range(vertices):
  row = [int(item) for item in input().split(" ")]
  Amat.append(row)
personX = int(input())
personY = int(input())
print(findConnectionLevel(vertices, Amat, personX, personY))


from collections import deque
class myStack:
  def __init__(self):
    self.stack = deque()
  
  def pop(self):
    return self.stack.pop()
  
  def push(self, x):
    return self.stack.append(x)

  def isEmpty(self):
    return False if self.stack else True

def runDFSForTankT(tanks, GList, t, visited):
  s = myStack()
  s.push(t)
  visited[t] = True

  while not s.isEmpty():
    i = s.pop()
    for p in GList[i]:
      if not visited[p]:
        s.push(p)
        visited[p] = True;

def findMasterTank(tanks, pipes):
  GList = {}
  for i in tanks:
    GList[i]=[]
  for (i,j) in pipes:
    GList[i].append(j)

  visited = {t:False for t in tanks}
  
  lastVisited = tanks[0] 
  for t in tanks:
    if not visited[t]:
      runDFSForTankT(tanks, GList, t, visited)
      lastVisited = t

  visited = {t:False for t in tanks}
  runDFSForTankT(tanks, GList, lastVisited, visited)

  for v in visited:
    if not visited[v]:
      return 0
  return lastVisited

# GRPA 2

v = [item for item in input().split(" ")]
#Tanks(vertices) numbered from 1 to n in string format.
numberOfEdges = int(input())
e = []
for i in range(numberOfEdges):
  s = input().split(" ")
  e.append((s[0], s[1]))
print(findMasterTank(v, e))

# GRPA 3

class Queue:
  def __init__(self):
    self.queue = []

  def addq(self, v):
    self.queue.append(v)

  def delq(self):
    v = None
    if not self.isempty():
      v = self.queue[0]
      self.queue = self.queue[1:]
      return v

  def isempty(self):
    return self.queue == []

  def __str__(self):
    return str(self.queue)
 
def dInv(d): 
  d_ = {}
  if not isinstance(list(d.values())[0], list):
    for k, v in d.items():
      if v not in d_:
        d_[v] = []
      d_[v].append(k)
    return d_

  if isinstance(list(d.values())[0], list):
    for k, v in d.items():
      for v_ in v:
        if v_ not in d_:
          d_[v_] = []
        d_[v_].append(k)
    return d_

def longestpathlist(AList): 
  indegree, lpath = {}, {}
  for u in AList:
    indegree[u], lpath[u] = 0, 0
  for u in AList:
    for v in AList[u]:
      indegree[v] = indegree[v] + 1
  
  zerodegreeq = Queue()
  for u in AList:
    if indegree[u] == 0:
      zerodegreeq.addq(u)
  
  while not zerodegreeq.isempty():
    j = zerodegreeq.delq()
    indegree[j] = indegree[j] - 1
    for k in AList[j]:
      indegree[k] = indegree[k] - 1
      lpath[k] = max(lpath[k], lpath[j] + 1)
      if indegree[k] == 0:
        zerodegreeq.addq(k)
  return lpath
  
def longJourney(AList):
  lpath = longestpathlist(AList) 
  IAList = dInv(AList) 
  Ilj = dInv(lpath) 

  maxVal = max(lpath.values()) 
  prev = Ilj[maxVal][0] 
  path = [prev] 
  for i in range(maxVal, -1, -1):
    for p in Ilj[i]: 
      if p in IAList[prev]: 
        path.append(p) 
        prev = p
  return path[::-1]
