def bfs(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    Q = []
    Q.append((x, y))
    visited[x][y] = 0
    while len(Q) != 0:
        x, y = Q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= H: continue
            if ny < 0 or ny >= W: continue
            if data[nx][ny] == 0: continue
            if data[x][y] == 2:
                if nx != x+1 or nx != x-1 and ny != y: continue
            elif data[x][y] == 3:
                if ny != y+1 or ny != y-1 and nx != x: continue
            elif data[x][y] == 4:
                if nx != x-1 and ny != y+1: continue
            elif data[x][y] == 5:
                if nx != x+1 and ny != y+1: continue
            elif data[x][y] == 6:
                if nx != x+1 and ny != y-1: continue
            elif data[x][y] == 7:
                if nx != x-1 and ny != y-1: continue
            elif visited[x][y] >= Time: continue

            D = visited[x][y] + 1
            if D < visited[nx][ny]:
                visited[nx][ny] = D
                Q.append((nx, ny))


import sys
sys.stdin = open('탈주범.txt')

T = int(input())
for tc in range(1, T+1):
    H, W, HL, WL, Time = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(H)]
    visited = [[987654321 for _ in range(W)] for _ in range(H)]
    cnt = 0
    bfs(HL, WL)


    for i in range(H):
        for j in range(W):
            if 0 < visited[i][j] <= Time:
                cnt += 1

    print('#{} {}'.format(tc, cnt))