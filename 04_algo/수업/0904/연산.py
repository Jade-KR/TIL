import sys
sys.stdin = open('연산.txt')

T = int(input())
for tc in range(1, T+1):
    p, q = map(int, input().split())

    n = 1
    cnt = 0
    while n <= 40000:
        n = n + cnt*4
        cnt += 1

    max_x, max_y = cnt-1, cnt-1

    G = [[0 for _ in range(300)] for _ in range(300)]

    for i in range(1, 290):
        for j in range(1, 290):
            if j == 1 and i == 1:
                G[i][j] = 1
            elif j == 1:
                G[i][j] = G[i-1][j] + i-1
            else:
                G[i][j] = G[i][j-1] + j + (i-1)

    gx = 0
    gy = 0
    for y in range(290):
        for x in range(290):
            if G[y][x] == p:
                gx += x
                gy += y
            if G[y][x] == q:
                gx += x
                gy += y

    print('#{} {}'.format(tc, G[gy][gx]))