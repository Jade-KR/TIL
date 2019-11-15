import sys
sys.stdin = open('두더지.txt')

def dfs(x, y):
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n:
            continue

        if visited[new_y][new_x] != 0 or data[new_y][new_x] == 0:
            continue

        visited[new_y][new_x] = 1

        dfs(new_x, new_y)

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]




cnt = 0
for i in range(n):
    for j in range(n):
        if data[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            dfs(j, i)
            cnt += 1

print(cnt)
