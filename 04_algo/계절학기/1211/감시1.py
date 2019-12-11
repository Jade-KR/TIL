import sys
sys.stdin = open("감시.txt")
import collections


def bfs(x, y, d):
    global ans, safe
    q = collections.deque()
    q.append((x, y))
    visited[x][y] = 1
    while len(q):
        nx, ny = q.popleft()
        for v in range(4):



    safe = 0
    for w in range(N):
        for e in range(M):
            if visited[w][e] == 0 and office[w][e] == 0:
                safe += 1
    if ans > safe:
        ans = safe

def perm(arr=[]):
    global visited
    if len(arr) == cnt:
        print(arr)
        visited = [[0] * M for _ in range(N)]
        for k in range(cnt):
            d = arr[k]
            x, y = cctv[k]
            bfs(x, y, d)

    else:
        for i in range(4):
            arr.append(data[i])
            perm(arr)
            arr.pop()



N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cctv = []
direction = []
cnt = 0
ans = 98765433321
safe = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]




for i in range(N):
    for j in range(M):
        if 0 < office[i][j] < 6:
            cnt += 1
            cctv.append((i, j))

data = [1, 2, 3, 4]

perm()
print(ans)