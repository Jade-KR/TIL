def snail(arr):
    global N
    newX, newY = 0, 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dr_s = 0
    num = 1

    for i in range(N*N):
        X, Y = newX, newY
        arr[Y][X] = num
        newX = dx + dx[dr_s]
        newY = dy + dy[dr_s]

        if newX >= N or newX < 0 or newY >= N or newY < 0 or arr[newY][newX] != 0:
            dr_s = (dr_s + 1) % 4





import sys
sys.stdin = open('dfs.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]

    snail(arr)

    print('#{}'.format(tc))

    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()
