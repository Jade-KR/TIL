def bfs(x, y):
    Q = []
    Q.append((x, y))
    visited[x][y] = 1
    while len(Q) != 0:
        x, y = Q.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= N: continue
            if ny < 0 or ny >= N: continue
            if M[nx][ny] >= M[x][y]: continue
            visited[nx][ny] = visited[x][y] + 1
            Q.append((nx, ny))


import sys
sys.stdin = open('등산로.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    M = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    result = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    max_m = 0
    x = 0
    y = 0
    for i in range(N):
        for j in range(N):
            if max_m < M[i][j]:
                max_m = M[i][j]

    for i in range(N):
        for j in range(N):
            if M[i][j] == max_m:
                x = i
                y = j
                for k in range(K+1):
                    for z in range(N):
                        for c in range(N):
                            M[z][c] -= k
                            visited = [[0 for _ in range(N)] for _ in range(N)]
                            bfs(x, y)
                            M[z][c] += k
                            for q in range(N):
                                for w in range(N):
                                    if result < visited[q][w]:
                                        result = visited[q][w]

    print('#{} {}'.format(tc, result))