import copy

def width(x, y):
    global N, K, cnt

    nx, ny = x, y
    p_w[nx][ny] = 2

    for _ in range(N):
        ny += 1
        if ny >= N or ny < 0 or p_w[nx][ny] == 0:
            L = ny - y
            if L == K:
                cnt += 1
            break
        else:
            p_w[nx][ny] = 2

def height(x, y):
    global N, K, cnt

    nx, ny = x, y
    p_h[nx][ny] = 2

    for _ in range(N):
        nx += 1
        if nx >= N or nx < 0 or p_h[nx][ny] == 0:
            L = nx - x

            if L == K:
                cnt += 1
            break
        else:
            p_h[nx][ny] = 2



import sys
sys.stdin = open('단어.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    p_w = [list(map(int, input().split())) for _ in range(N)]
    p_h = copy.deepcopy(p_w)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if p_w[i][j] == 1:
                x, y = i, j
                width(x, y)

    for i in range(N):
        for j in range(N):
            if p_h[i][j] == 1:
                x, y = i, j
                height(x, y)
    print('#{} {}'.format(tc, cnt))