from collections import deque

R, C = map(int, input().split())
maze = [list(map(str, input())) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
q = deque()
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            jx, jy = i, j
        elif maze[i][j] == 'F':
            q.append((i, j, 1))
            visited[i][j] = 1

def bfs():
    q.append((jx, jy, 0))
    visited[jx][jy] = 1
    while q:
        x, y, f = q.popleft()
        for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                if f:
                    continue
                print(visited[x][y])
                return
            if not visited[nx][ny] and maze[nx][ny] != '#':
                q.append((nx, ny, f))
                visited[nx][ny] = visited[x][y]+1
    print("IMPOSSIBLE")

bfs()