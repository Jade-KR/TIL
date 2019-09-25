def bfs(v):
    global cnt
    cnt += 1
    Q = []
    Q.append(v)
    visited[v] = 1
    while len(Q) != 0:
        t = Q.pop(0)
        for w in range(1, N+1):
            if adj[t][w] == 1 and visited[w] == 0:
                visited[w] = 1
                Q.append(w)
    for j in range(1, len(visited)):
        if visited[j] == 0:
            bfs(j)


import sys
sys.stdin = open('마을무리.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num = [list(map(int, input().split())) for _ in range(M)]
    adj = [[0 for _ in range(N+1)] for _ in range(N+1)]
    visited = [0] * (N+1)
    cnt = 0
    for i in range(len(num)):
        adj[num[i][0]][num[i][1]] = 1
        adj[num[i][1]][num[i][0]] = 1

    bfs(1)
    print('#{} {}'.format(tc, cnt))