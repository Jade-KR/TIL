import sys
import collections
sys.stdin = open('게리맨더링.txt')

def bfs(w):
    global check, flag
    flag = 0
    check = []
    check.append(w)
    visited = [0] * (N + 1)
    q = collections.deque()
    q.append(w)
    visited[w] = 1
    while q:
        t = q.popleft()
        for o in range(1, N+1):
            if visited[o] == 1 or adj[t][o] == 0:
                continue
            visited[o] = 1
            q.append(o)
            check.append(o)

    if check in g1:
        flag = 1


def powerset(n, dep):
    if n == dep:
        g1 = []
        g2 = []
        for i in range(n):
            if A[i] == 1:
                g1.append(arr[i])
            else:
                g2.append(arr[i])
        print(g1)
        print(g2)
        print()
        if g1:
            for i in g1:
                bfs(i)
        if g2:
            for j in g2:
                bfs(j)
    else:
        A[dep] = 1
        powerset(n, dep+1)
        A[dep] = 0
        powerset(n, dep+1)


N = int(input())
people = list(map(int, input().split()))
info = [list(map(int, input().split())) for _ in range(N)]
adj = [[0] * (N+1) for _ in range(N+1)]
visited = [[0] * (N+1) for _ in range(N+1)]

for i in range(N):
    for j in range(1, len(info[i])):
        adj[i+1][info[i][j]] = 1

arr = [i+1 for i in range(N)]
A = [0] * N

powerset(6, 0)