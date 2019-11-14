import sys
import collections
sys.stdin = open('탈주범.txt')

def validator(x, y, nx, ny):
    global check
    check = 0
    for i in direction[data[nx][ny]]:
        cx = nx + dx[i]
        cy = ny + dy[i]

        if cx < 0 or cx >= N or cy < 0 or cy >= M:
            continue
        if cx == x and cy == y:
            check = 1
            return

def bfs(x, y):
    if L == 1:
        visited[x][y] = 1
        return
    q = collections.deque()
    visited[x][y] = 1
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for k in direction[data[x][y]]:
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny]:
                continue
            if data[nx][ny] == 0:
                continue
            validator(x, y, nx, ny)
            if check == 1:
                visited[nx][ny] = visited[x][y] + 1
                if visited[nx][ny] < L:
                    q.append((nx, ny))


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    cnt = 0

    direction = {
        1: [0, 1, 2, 3],
        2: [0, 1],
        3: [2, 3],
        4: [0, 3],
        5: [1, 3],
        6: [1, 2],
        7: [0, 2]
    }


    bfs(R, C)

    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                cnt += 1
    print('#{} {}'.format(tc, cnt))
