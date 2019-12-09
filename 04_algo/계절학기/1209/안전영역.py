import sys
sys.stdin = open('안전영역.txt')
import collections

def bfs(x, y, r):
    global cnt
    q = collections.deque()
    visited[x][y] = 1
    q.append((x, y))
    while len(q):
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if visited[nx][ny] == 1 or area[nx][ny] <= r: continue
            visited[nx][ny] = 1
            q.append((nx, ny))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
min_a = 987654321
max_a = 0
ans = 0
for i in range(N):
    for j in range(N):
        if area[i][j] < min_a:
            min_a = area[i][j]
        if area[i][j] > max_a:
            max_a = area[i][j]

rain = [r for r in range(min_a-1, max_a+1)]

for r in rain:
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] > r and visited[i][j] == 0:
                bfs(i, j, r)
                cnt += 1
    if ans < cnt:
        ans = cnt

print(ans)