import sys
sys.stdin = open('탈출.txt')
import collections

def bfs():
    global ans
    while len(q):
        x, y, obj, what = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < R and 0 <= ny < C and data[nx][ny] != 'X':
                if obj == 'L':
                    if data[nx][ny] == 'D':
                        if ans < what:
                            ans = what
                            return
                    elif visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny, obj, what+1))
                elif obj == 'W':
                    if visited[nx][ny] != 'W' and data[nx][ny] != 'D':
                        visited[nx][ny] = 'W'
                        q.append((nx, ny, obj, what))



R, C = map(int, input().split())
data = [list(map(str, input())) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
q = collections.deque()
ans = -1
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(R):
    for j in range(C):
        if data[i][j] == '*':
            visited[i][j] = 'W'
            q.append((i, j, 'W', 'W'))

for i in range(R):
    for j in range(C):
        if data[i][j] == 'S':
            visited[i][j] = 1
            q.append((i, j, 'L', 1))

bfs()
if ans == -1:
    ans = 'KAKTUS'

print(ans)