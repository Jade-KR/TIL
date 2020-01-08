import sys
sys.stdin = open('cctv.txt')

def bfs(x, y):
    global min_c, cnt
    Q = []
    Q.append((x, y))
    while len(Q) != 0:
        x, y = Q.pop(0)
        if data[x][y] == 1:
            for k in range(4):
                cnt = 0
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    break
                if data[nx][ny] == 6:
                    break
                visited[nx][ny] = 7
            for k in range(N):
                for o in range(M):
                    if data[k][o] == 7:
                        cnt += 1
            if min_c <
            min_c = cnt



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    camera = [1, 2, 3, 4, 5]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    min_c = 0


    for i in range(N):
        for j in range(M):
            if data[i][j] in camera:
                min_c = 0
                cnt = 0
                bfs(i, j)
