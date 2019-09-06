def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1

    while q:
        t = q.pop(0)
        for w in range(1, V+1):
            if adj[t][w] == 1 and visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1


import sys
sys.stdin = open('prac.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    adj = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for i in range(E):
        adj[info[i][0]][info[i][1]] = 1
        adj[info[i][1]][info[i][0]] = 1


    bfs(S)

    result = visited[G] - 1
    if result == -1:
        result = 0

    print('#{} {}'.format(tc, result))