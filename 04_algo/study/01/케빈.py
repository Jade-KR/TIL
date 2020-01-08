import sys
sys.stdin = open('케빈.txt')
import collections

def bfs(v):
    global stack, cabin
    q = collections.deque()
    visited[v] = 1
    q.append((v, stack))
    while len(q):
        t, s = q.popleft()
        for w in range(1, N+1):
            if visited[w] == 1 or adj[t][w] == 0: continue
            visited[w] = 1
            cabin += s
            q.append((w, s+1))

N, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(M)]
adj = [[0]*(N+1) for _ in range(N+1)]
min_c = 987655443

for i in range(M):
    adj[info[i][0]][info[i][1]] = 1
    adj[info[i][1]][info[i][0]] = 1

for a in range(1, N+1):
    visited = [0] * (N + 1)
    stack = 1
    cabin = 0
    bfs(a)
    if min_c > cabin:
        min_c = cabin
        ans = a

print(ans)