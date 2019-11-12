import sys
sys.stdin = open('prac.txt')

def dfs(x, y):
    visited[x][y] = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        elif visited[nx][ny] == 1 or data[nx][ny] == 1:
            continue
        visited[nx][ny] = 1
        dfs(nx, ny)




def com(dep=0):
    global data, visited, cnt, min_c
    if len(arr) == 3:
        for q in range(3):
            data[arr[q][0]][arr[q][1]] = 1

        for o in range(N):
            for p in range(M):
                if data[o][p] == 2:
                    visited = [[0] * M for _ in range(N)]
                    cnt = 0
                    cnt2 = 0
                    dfs(o, p)
                    for a in range(N):
                        for b in range(M):
                            if visited[a][b] == 0:
                                cnt += 1
                            if data[a][b] == 1:
                                cnt2 += 1
                    if min_c < cnt:
                        min_c = cnt - cnt2
        return
    if dep == len(wall):
        return
    for i in range(dep, len(wall)):
        arr.append(wall[i])
        com(i+1)
        arr.pop()

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]* M for _ in range(N)]
wall = []
arr = []
min_c = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for a in range(N):
    for b in range(M):
        if data[a][b] == 0:
            wall.append([a, b])

com()

print(min_c)