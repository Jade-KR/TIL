def bfs(x, y):
    global arr, visited
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = []
    q.append((x, y))
    visited[x][y] = 1
    while len(q) != 0:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny < 0 or ny == 100: continue
            if nx < 0 or nx == 100: continue
            if arr[nx][ny] == 3:
                return 1
            elif arr[nx][ny] == 0 and visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = 1
    return 0


import sys
sys.stdin = open('미로2.txt')

T = 10
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(100)]
    visited = [[0 for _ in range(100)] for _ in range(100)]

    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                x, y = i, j

    print('#{} {}'.format(tc, bfs(x, y)))