def bfs(v):
    global cnt
    cnt += 1
    q = []
    q.append(v)
    visited[v] = 1

    while len(q) != 0:
        t = q.pop(0)
        for w in range(1, N+1):
            if adj[t][w] == 1 and visited[w] == 0:
                q.append(w)
                visited[w] = 1
    for i in range(1, len(visited)):
        if visited[i] == 0:
            bfs(i)

import sys
sys.stdin = open('그룹나누기.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    adj = [[0 for _ in range(N+1)] for _ in range(N+1)]
    visited = [0]*(N+1)
    cnt = 0


    for i in range(0, len(data)-1, 2):
        adj[data[i]][data[i+1]] = 1
        adj[data[i+1]][data[i]] = 1

    bfs(data[0])
    cnt += visited.count(0) - 1
    print('#{} {}'.format(tc, cnt))