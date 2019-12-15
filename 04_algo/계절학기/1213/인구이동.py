import sys
sys.stdin = open("인구이동.txt")
import collections

def bfs(x, y):
    global chk
    q = collections.deque()
    visited[x][y] = 1
    q.append((x, y))
    while len(q):
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if visited[nx][ny] != 0: continue
            if L <= abs(population[nx][ny] - population[x][y]) <= R:
                share[nx][ny] = alians
                share[x][y] = alians
                visited[nx][ny] = 1
                q.append((nx, ny))
                chk = 1


N, L, R = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]
check = 0
ans = -1
chk = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


while check == 0:
    alians = 1
    cnt = 0
    check = 1
    visited = [[0] * N for _ in range(N)]
    share = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                bfs(i, j)
                if chk == 1:
                    alians += 1
                    chk = 0
                    check = 0

    ans += 1
    for c in range(1, alians):
        tmp = 0
        avg = 0
        cnt = 0
        for a in range(N):
            for b in range(N):
                if share[a][b] == c:
                    cnt += 1
                    tmp += population[a][b]


        if cnt != 0:
            avg = int(tmp / cnt)
            for a in range(N):
                for b in range(N):
                    if share[a][b] == c:
                        population[a][b] = avg
        else:
            check = 1
print(ans)