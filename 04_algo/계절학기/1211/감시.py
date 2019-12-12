import sys
sys.stdin = open("감시.txt")
import collections

def bfs(x, y, num, d):
    q = collections.deque()

    visited[x][y] = 1
    # cctv 번호별, 감시할 방향 체크
    if num == 1:
        direc = [d]
    elif num == 2:
        direc = [d, (d+2)%4]
    elif num == 3:
        direc = [d, (d+1)%4]
    elif num == 4:
        direc = [(d+2)%4, d, (d+1)%4]
    elif num == 5:
        direc = [0,1,2,3]

    #방향에 맞게 감시
    for dd in direc:
        q.append((x, y))
        while len(q):
            nx, ny = q.popleft()
            # 오른쪽 방향 감시
            if dd == 0:
                if ny < M-1 and office[nx][ny+1] != 6:
                    if office[nx][ny + 1] == 0:
                        visited[nx][ny+1] = 1
                    q.append((nx, ny+1))
            # 아래쪽 방향 감시
            elif dd == 1:
                if nx < N-1 and office[nx+1][y] != 6:
                    if office[nx + 1][y] == 0:
                        visited[nx+1][ny] = 1
                    q.append((nx+1, ny))
            # 왼쪽 방향 감시
            elif dd == 2:
                if ny > 0 and office[nx][ny-1] != 6:
                    if office[nx][ny - 1] == 0:
                        visited[nx][ny-1] = 1
                    q.append((nx, ny-1))
            # 위쪽 방향 감시
            elif dd == 3:
                if nx > 0 and office[nx-1][ny] != 6:
                    if office[nx-1][ny] == 0:
                        visited[nx-1][ny] = 1
                    q.append((nx-1, ny))




def perm(arr=[]):
    global visited, ans, safe
    if len(arr) == cnt:
        visited = [[0] * M for _ in range(N)]
        for k in range(cnt):
            d = arr[k] # k 번째 cctv의 방향
            x, y, num = cctv[k] # k 번째 cctv의 좌표와 번호
            bfs(x, y, num, d)

        safe = 0
        for w in range(N):
            for e in range(M):
                if visited[w][e] == 0 and office[w][e] == 0:
                    safe += 1
        if ans > safe:
            ans = safe
    else:
        for i in range(4):
            arr.append(data[i])
            perm(arr)
            arr.pop()

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cctv = []
cnt = 0
ans = 0
safe = 0

for i in range(N):
    for j in range(M):
        if 0 < office[i][j] < 6:
            cnt += 1 # cctv의 개수
            cctv.append((i, j, office[i][j])) # cctv의 좌표, cctv 번호
        if 0 == office[i][j]:
            ans += 1 # cctv가 없을 때 사각지대 체크해야하기 때문에 체크

data = [0, 1, 2, 3]
perm()

print(ans)