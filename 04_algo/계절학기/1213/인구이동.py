import sys
sys.stdin = open("인구이동.txt")
import collections

def bfs(x, y):
    q = collections.deque()
    visited[i][j] = 1
    q.append((x, y))
    while len(q):
        global check
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if visited[nx][ny] != 0: continue
            visited[nx][ny] = 1
            if L <= abs(population[x][y] - population[nx][ny]) <= R:
                visited[nx][ny] = 2
                visited[x][y] = 2
            q.append((nx, ny))

    check = 1
    for a in range(N):
        for b in range(N):
            if visited[a][b] == 2:
                check = 0

N, L, R = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
check = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while check==0:
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                bfs(i, j)
    cnt = 0
    tmp = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 2:
                tmp += population[i][j]
                cnt += 1
    avg = int(tmp/cnt)