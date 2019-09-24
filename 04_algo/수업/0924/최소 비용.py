def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = []
    q.append((x, y))
    visited[x][y] = 0
    while len(q) != 0:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N: continue
            if ny < 0 or ny >= N: continue
            if H[nx][ny] > H[x][y]:
                D = visited[x][y] + 1 + H[nx][ny] - H[x][y]
            else:
                D = visited[x][y] + 1
            if D < visited[nx][ny]:
                visited[nx][ny] = D
                q.append((nx, ny))




import sys
sys.stdin = open("최소 비용.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]
    visited = [[987654321 for _ in range(N)] for _ in range(N)]
    cnt = 0
    bfs(0, 0)
    print('#{} {}'.format(tc, visited[N-1][N-1]))