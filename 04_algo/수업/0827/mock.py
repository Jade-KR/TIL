import sys
sys.stdin = open('mock.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(K)]
    cmp = [[0 for _ in range(M)] for _ in range(N)]
    color = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tmp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(K):
        #좌표 리셋
        x = []
        y = []
        for j in range(5):
            if j == 0 or j == 2:
                x.append(data[i][j])
            if j == 1 or j == 3:
                y.append(data[i][j])

        for k in range(y[0], y[1]):
            for l in range(x[0], x[1]):
                if cmp[k][l] <= data[i][4]:
                    cmp[k][l] = data[i][4]

    if cmp[k][l] > data[i][4]:
        break
    for z in range(N):
        for m in range(M):
            for o in color:
                if cmp[z][m] == o:
                    tmp[o] += 1
    print('#{} {}'.format(tc, max(tmp)))