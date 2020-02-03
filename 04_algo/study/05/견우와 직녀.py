import sys
sys.stdin = open('견우와 직녀.txt')
import collections

def bfs(x, y):
    global K, tmp, min_m
    q = collections.deque()
    q.append((x, y, K))
    visited[x][y] = 1
    while len(q):
        x, y, NK = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if NK == 0:
                    tmp = 1
                if (NK+tmp) % M == 0 or NK == bridge[nx][ny]:
                    if NK == 0:
                        tmp = 0
                    if nx == N-1 and ny == N-1:
                        if min_m > NK:
                            min_m = NK
                    visited[nx][ny] = 1
                    q.append((nx, ny, NK+1))
                else:
                    if bridge[nx][ny] == 1:
                        if nx == N - 1 and ny == N - 1:
                            if min_m > NK:
                                min_m = NK
                        visited[nx][ny] = 1
                        q.append((nx, ny, NK+1))


N, M = map(int, input().split())
bridge = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
min_m = 987654321
K = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
tmp = 0

bfs(0, 0)

print(min_m)