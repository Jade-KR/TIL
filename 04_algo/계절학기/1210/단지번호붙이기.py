import sys
sys.stdin = open('단지번호붙이기.txt')

def dfs(x, y):
    visited[x][y] = cnt
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
        if visited[nx][ny] != 0 or data[nx][ny] == 0: continue
        visited[nx][ny] = 1
        dfs(nx, ny)

N = int(input())
data = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0
result = []
for i in range(N):
    for j in range(N):
        if data[i][j] != 0 and visited[i][j] == 0:
            cnt += 1
            dfs(i, j)

print(cnt)

for i in range(cnt):
    ans = 0
    for a in range(N):
        for b in range(N):
            if visited[a][b] == i+1:
                ans += 1
    result.append(ans)

result = sorted(result)
for k in result:
    print(k)