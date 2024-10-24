# GRPA 1

def insertionsort(L): #use this because it is stable sort
    n = len(L)
    if n < 1:
        return(L)
    for i in range(n):
        j = i
        while(j > 0 and L[j][1] > L[j-1][1]):
            (L[j],L[j-1]) = (L[j-1],L[j])
            j = j-1
    return(L)

def DishPrepareOrder(order_list):
    order_count = {}
    R = []
    for order in order_list:
        if order in order_count:
            order_count[order] += 1
        else:
            order_count[order] = 1
    for ID in sorted(order_count.keys()):
        R.append((ID,order_count[ID]))
    R=insertionsort(R)
    Res = []
    for tup in R:
        Res.append(tup[0])
    return Res
nums = eval(input())
print(DishPrepareOrder(nums))

# GRPA 2

class create_stack:
  def __init__(self):
    self.stack = []
  def push(self,d):
    self.stack += [d]
  def pop(self):
    t = self.stack[-1]
    self.stack = self.stack[:-1]
    return t

def EvaluateExpression(exp):
  opt = ['+','-','*','/','**']
  stk = create_stack()
  L = exp.split(' ')
  for i in L:
    if i not in opt:
      stk.push(i)
    else:
      b = stk.pop()
      a = stk.pop()
      res = eval(a + i + b)
      stk.push(str(res))
  return stk.pop()
print(float(EvaluateExpression(input())))

# GRPA 3

def reverse(root):
  if (root.isEmpty()):
    return root
  temp = root
  prev = None
  while (temp):
    next, temp.next = temp.next, prev
    prev, temp = temp, next
  return prev
