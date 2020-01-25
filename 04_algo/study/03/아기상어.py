import sys
sys.stdin = open('아기상어.txt')
import collections

def bfs(x, y):
    global stomach, time, sx, sy, check
    choice = []
    distance = 987654321
    visited[x][y] = 1
    q = collections.deque()
    q.append((x, y))
    while len(q):
        x, y = q.popleft()
        if distance <= visited[x][y]:
            break
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and location[nx][ny] <= shark and visited[nx][ny] == 0:
                if location[nx][ny] in target:
                    visited[nx][ny] = visited[x][y] + 1
                    choice.append([nx, ny, visited[nx][ny]])
                    distance = visited[nx][ny]
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))


    if len(choice):
        num = 0
        h = 987643334
        w = 987654321
        for a in range(len(choice)):
            if choice[a][0] < h:
                h = choice[a][0]
                w = choice[a][1]
                num = a
            elif choice[a][0] == h:
                if choice[a][1] <= w:
                    num = a
        location[choice[num][0]][choice[num][1]] = 0
        stomach += 1
        time += visited[choice[num][0]][choice[num][1]] - 1
        sx, sy = choice[num][0], choice[num][1]
    else:
        check = 1

N = int(input())
location = [list(map(int, input().split())) for _ in range(N)]
shark = 2
stomach = 0
check = 0
time = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(N):
    for j in range(N):
        if location[i][j] == 9:
            sx, sy = i, j
            location[i][j] = 0
            break

while check == 0:
    if stomach == shark:
        shark += 1
        stomach = 0
    target = [i for i in range(1, shark)]
    visited = [[0] * N for _ in range(N)]
    bfs(sx, sy)

print(time)