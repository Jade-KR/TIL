import sys
sys.stdin = open('욕심쟁이판다.txt')

sys.getrecursionlimit()

def dfs(x, y):
    if memo[x][y]:
        return memo[x][y]
    memo[x][y] = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if data[x][y] < data[nx][ny]:
                memo[x][y] = max(memo[x][y], dfs(nx, ny) + 1)
    return memo[x][y]

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
memo = [[0]*N for _ in range(N)]
ans = 1
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(N):
    for j in range(N):
        if memo[i][j] == 0:
            memo[i][j] = dfs(i, j)


for i in range(N):
    for j in range(N):
        ans = max(ans, memo[i][j])

print(ans)