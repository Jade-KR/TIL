def bfs(v):
    q = []
    visited[v] = 1
    q.append(v)
    print(v, end=' ')

    while len(q) != 0:
        t = q.pop(0)
        for w in range(1, N+1):
            if adj[t][w] == 1 and visited[w] == 0:
                q.append(w)
                visited[w] = 1
                print(w, end=' ')


import sys
sys.stdin = open('bfs.txt')

N, E = map(int, input().split())
info = list(map(int, input().split()))
adj = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for i in range(0, len(info), 2):
    adj[info[i]][info[i+1]] = 1
    adj[info[i+1]][info[i]] = 1

bfs(1)