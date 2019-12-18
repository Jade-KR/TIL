import sys
sys.stdin = open('보물섬.txt')
import collections

def bfs(x, y):
    global ans
    q = collections.deque()
    visited[x][y] = 1
    q.append((x, y))

    while len(q):
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if visited[nx][ny] != 0 or data[nx][ny] == 'W': continue
            visited[nx][ny] = visited[x][y] + 1
            if visited[nx][ny] > ans:
                ans = visited[nx][ny]
            q.append((nx, ny))

N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    for j in range(M):
        if data[i][j] == 'L':
            visited = [[0] * M for _ in range(N)]
            bfs(i, j)

print(ans-1)