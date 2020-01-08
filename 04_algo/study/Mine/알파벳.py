import sys
sys.stdin = open('알파벳.txt')

def dfs(x, y, cnt):
    global max_c
    if cnt > max_c:
        max_c = cnt
    check.append(data[x][y])
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or nx >= R or ny < 0 or ny >= C: continue
        if data[nx][ny] in check: continue
        cnt += 1
        dfs(nx, ny, cnt)
        cnt -= 1
        check.pop()


R, C = map(int, input().split())
data = [list(map(str, input())) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
max_c = -9876654332
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(C):
    visited = [[0] * C for _ in range(R)]
    check = []
    dfs(0, i, 0)

print(max_c)