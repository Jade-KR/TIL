LIFO : Stack

FIFO : Que



스택의 push 알고리즘

append로 데이터를 삽입

```python
def push(item):
    s.append(tiem)
```



스택의 pop알고리즘

```python
def pop():
    if len(s) == 0:
        return
    else:
        return s.pop(-1)
```


```python
s = list()
def push(item):
    s.append(item)
def pop():
    if len(s) == 0:
        return
    else:
        return s.pop(-1)
def isEmpty():
    if len(s) == 0:
        return True
    else:
        return False

def check_matching(data):
    for i in range(len(data)):
    if data[i] == '(':
        stack.append('(')
    elif data[i] == ')':
        stack.pop()
    if not isEmpty():
        return False
    else:
        return True
    
data = input()
print(check_matching(data))
```

재귀호출(팩토리얼)

```python
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
```

재귀호출(피보나치)

```python
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
```

Memoization

```python
def fibo(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]

memo = [0, 1]
print(fibo(100))
```

fibo2

```python
def fibo2(n):
    f = [0, 1]

    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])

    return f[n]

print(fibo2(7))
```



DFS(깊이우선탐색)

stack을 따로 만들거나 재귀를 하거나

```python
DFS_Recursie(G, v):
    visited[v] = True
    
    for each all w in adjacency(G, v):
        if visited[w] != True
        DFS_Recursive(G, w)
```

dfs(v)

visited[v] = 1

for v정점 인접한 정점(w)

​	if visited[w] != 1

​		dfs(w)



인접행렬(그래프를 나타낼 수 있음)을 먼저 저장해야함.

```python
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
# def dfs(v):
#     if s:
#
#         for i in range(1, n+1):
#             if box[i]:
#                 visited[i] = 1
#                 s.append(i)

def dfs(v):
    visited[v] = 1
    print(v, end=" ")

    for w in range(n+1):
        if box[v][w] == 1 and visited[w] == 0:
            dfs(w)



n, m = map(int, input().split())

line = list(map(int, input().split()))

box = [[0 for _ in range(n+1)] for _ in range(n+1)]

visited = [0 for i in range(n+1)]

for i in range(0, len(line), 2):
    box[line[i]][line[i+1]] = 1
    box[line[i+1]][line[i]] = 1

for i in range(n+1):
    print("{} {}".format(i, box[i]))
s = [n]
dfs(1)
```

pop을 할때 비어있는 것 꺼내지 않도록 조심해야함. (length를 이용해서 방지해야함)

```python
def dfs():
   global v
   while st:
       print(K[v])
       for k in range(len(nl)):
           if (not vl[nl[k][1]-1]) and v == nl[k][0]:
               st.append(nl[k][1])
               vl[nl[k][1]-1] = 1
           if (not vl[nl[k][0]-1]) and v == nl[k][1]:
               st.append(nl[k][0])
               vl[nl[k][0]-1] = 1
       v = st.pop()
N = 7
vl = [0 for i in range(N)]
nl = [[1,2], [1,3],[2,4],[2,5],[3,5],[4,6],[5,6],[6,7]]
K = [0,'A','B','C','D','E','F','G']
v = 1
vl[v-1] = 1
st = []
st.append(v)
dfs()
```

