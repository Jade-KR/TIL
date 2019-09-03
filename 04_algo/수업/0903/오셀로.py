def

import sys
sys.stdin = open('오셀로.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    p = [[0 for _ in range(N)] for _ in range(N)]
    w, b = 0, 0

    p[N // 2 - 1][N // 2 - 1] = 2
    p[N // 2 - 1][N // 2] = 1
    p[N // 2][N // 2 - 1] = 1
    p[N // 2][N // 2] = 2

    dx = [0, 1, 0, -1, 1, -1, 1, -1]
    dy = [1, 0, -1, 0, 1, 1, -1, -1]

    for i in range(N):
        for j in range(N):
            print(p[i][j], end=" ")
        print()

    for i in range(M):
        p[data[i][0]-1][data[i][1]-1] = data[i][2]
        for j in range(8):
            if 
            if p[data[i][0] - 1+dx[j]][data[i][1] - 1 + dy[j]] != data[i][2]:



    for i in range(N):
        for j in range(N):
            print(p[i][j], end=" ")
        print()

    # for i in range(N):
    #     for j in range(N):
    #         if data[i][j] == 1:
    #             b += 1
    #         elif data[i][j] == 2:
    #             w += 1
    #
    # print('#{} {} {}'.format(tc, b, w))
