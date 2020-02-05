import sys
sys.stdin= open("견우와 직녀.txt")
import collections

def checkTime(v, p):
    out = 0
    cnt = 1
    while out == 0:
        cmp = p * cnt
        if v <= cmp:
            return cmp
        cnt += 1


def checkSafe(x, y):
    if bridge[x][y] == 0:
        return 1
    else:
        return 0

def checkBuild(x, y):
    for i in range(4):
        bx = x + dx[i]
        by = y + dy[i]
        if 0 <= bx < N and 0 <= by < N:
            if bridge[bx][by] == 1 and visited[bx][by] == 0:
                return 1
    return 0

def bfs(x, y):
    global K, tmp, min_m
    q = collections.deque()
    visited[x][y] = K
    q.append((x, y, K, d, c))
    while len(q):
        x, y, NK, danger, chance = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0:
                    if bridge[nx][ny] == 1: # 길일 때
                        if nx == N-1 and ny == N-1:
                            if min_m > NK:
                                min_m = NK
                        visited[nx][ny] = NK
                        q.append((nx, ny, NK+1, 0, chance))

                    elif bridge[nx][ny] == 0 and danger == 0 and chance == 1: #다리가 없고 안전할 때
                        NK = checkTime(NK, M)
                        cb = checkBuild(nx, ny)
                        # 오작교가 교차하는 곳인지 체크
                        if cb == 1:
                            visited[nx][ny] = NK
                            chance = 0
                            q.append((nx, ny, NK+1, 1, chance))

                    elif bridge[nx][ny] > 1 and danger == 0: #주기가 정해진 다리가 있고 안전할때
                        NK = checkTime(NK, bridge[nx][ny])
                        cb = checkBuild(nx, ny)
                        if cb == 1:
                            visited[nx][ny] = NK
                            q.append((nx, ny, NK+1, 1, chance))

                elif visited[nx][ny]:
                    if visited[nx][ny] >= NK+1:
                        if bridge[nx][ny] == 1: # 길일 때
                            if nx == N-1 and ny == N-1:
                                if min_m > NK:
                                    min_m = NK
                            visited[nx][ny] = NK
                            q.append((nx, ny, NK+1, 0, chance))



N, M = map(int, input().split())
bridge = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
min_m = 987654321
c = 1
K = 0
d = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
tmp = 0

bfs(0, 0)

print(min_m)