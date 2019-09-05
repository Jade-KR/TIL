def dfs(v):
    visited[v] = 1
    print(v, end=' ')

    for w in range(N+1):
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w)

import sys
sys.stdin = open('dfs.txt')

N, M = map(int, input().split())
info = list(map(int, input().split()))
adj = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for i in range(0, len(info), 2):
    adj[info[i]][info[i+1]] = 1
    adj[info[i+1]][info[i]] = 1

dfs(1)