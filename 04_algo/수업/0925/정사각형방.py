dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(x, y):
    global min_d, result
    cnt = 1
    Q = []
    Q.append((x, y))
    while len(Q) != 0:
        x, y = Q.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= N: continue
            if ny < 0 or ny >= N: continue
            if data[nx][ny] != data[x][y] +1: continue
            Q.append((nx, ny))
            cnt += 1

    if cnt > 1:
        if min_d < cnt:
            min_d = cnt
            result = data[i][j]
        elif min_d == cnt:
            if result > data[i][j]:
                result = data[i][j]


import sys
sys.stdin = open('정사각형방.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    min_d = 0
    result = 0
    for i in range(N):
        for j in range(N):
            bfs(i, j)

    print('#{} {} {}'.format(tc, result, min_d))