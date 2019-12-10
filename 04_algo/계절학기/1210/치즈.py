import sys, collections
sys.stdin = open('치즈.txt')

def bfs(x, y):
    global check
    q = collections.deque()
    visited[x][y] = 1
    q.append((x, y))
    for k in range(4):
        cx = x + dx[k]
        cy = y + dy[k]
        if visited[cx][cy] == 2:
            visited[x][y] = 3

    while len(q):
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if visited[nx][ny] != 0 or data[nx][ny] == 0: continue
            visited[nx][ny] = 1
            q.append((nx, ny))
            for k in range(4):
                cx = nx + dx[k]
                cy = ny + dy[k]
                if visited[cx][cy] == 2:
                    visited[nx][ny] = 3


def air(x, y):
    q = collections.deque()
    visited[x][y] = 2
    q.append((x, y))
    while len(q):
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if visited[nx][ny] != 0 or data[nx][ny] != 0: continue
            visited[nx][ny] = 2
            q.append((nx, ny))

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
hour = 0
check = 0
cnt = 0

while check == 0:
    check = 1
    visited = [[0] * M for _ in range(N)]
    air(0, 0)
    hour += 1
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and data[i][j] != 0:
                for k in range(4):
                    cx = i + dx[k]
                    cy = j + dy[k]
                    if visited[cx][cy] == 2:
                        visited[i][j] = 3

    for i in range(N):
        for j in range(M):
            if visited[i][j] == 3:
                data[i][j] = 0

    for i in range(N):
        for j in range(M):
            if data[i][j] != 0:
                check = 0

for i in range(N):
    for j in range(M):
        if visited[i][j] == 3:
            cnt += 1
print(hour)
print(cnt)