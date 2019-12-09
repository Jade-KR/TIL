import sys
sys.stdin = open('빙산.txt')
import collections

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
year = 0
chk = 0

def bfs(x, y):
    q = collections.deque()
    q.append((x, y))
    visited[x][y] = 1
    for k in range(4):
        cx = x + dx[k]
        cy = y + dy[k]
        if data[cx][cy] == 0:
            visited[x][y] += 1

    while len(q):
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx > N or ny < 0 or ny > M: continue
            if visited[nx][ny] > 0 or data[nx][ny] == 0: continue
            visited[nx][ny] = 1

            for k in range(4):
                cx = nx + dx[k]
                cy = ny + dy[k]
                if data[cx][cy] == 0:
                    visited[nx][ny] += 1
            q.append((nx, ny))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while chk == 0:
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if data[i][j] > 0 and visited[i][j] == 0:
                bfs(i, j)
                cnt += 1

    for i in range(N):
        for j in range(M):
            if data[i][j]:
                data[i][j] = data[i][j] - visited[i][j] + 1
                if data[i][j] < 0:
                    data[i][j] = 0

    if cnt >= 2:
        chk = 1
        break
    year += 1

if cnt == 1:
    year = 0

print(year)