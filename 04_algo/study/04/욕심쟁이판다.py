import sys
sys.stdin = open('욕심쟁이판다.txt')
import collections

def cleanUp(x, y, k):
    if k == 0:
        if y+1 < N:
            visited[x][y+1] = 0
        if x-1 >= 0:
            visited[x-1][y] = 0
        if y-1 >= 0:
            visited[x][y-1] = 0

    elif k == 1:
        if x+1 < N:
            visited[x+1][y] = 0
        if x-1 >= 0:
            visited[x-1][y] = 0
        if y-1 >= 0:
            visited[x][y-1] = 0

    elif k == 2:
        if y+1 < N:
            visited[x][y+1] = 0
        if x+1 < N:
            visited[x+1][y] = 0
        if y-1 >= 0:
            visited[x][y-1] = 0

    elif k == 3:
        if y+1 < N:
            visited[x][y+1] = 0
        if x-1 >= 0:
            visited[x-1][y] = 0
        if x+1 < N:
            visited[x+1][y] = 0


def bfs(x, y):
    global ans
    q = collections.deque()
    t = 1
    q.append((x, y, t))
    visited[x][y] = 1
    while len(q):
        x, y, t = q.popleft()
        if t > ans:
            ans = t
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            cleanUp(x, y, k)

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and data[nx][ny] > data[x][y]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny, t+1))


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
ans = -98765454

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(N):
        visited = [[0]*N for _ in range(N)]
        bfs(i, j)

print(ans)

