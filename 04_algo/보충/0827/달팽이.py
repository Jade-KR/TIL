def solve(arr):
    global N
    newX, newY = 0, 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dir_state = 0
    num = 1
    for i in range(N*N):
        X, Y = newX, newY
        arr[Y][X] = num
        newX = X + dx[dir_state]
        newY = Y + dy[dir_state]

        if newY >= N or newX >= N or newY < 0 or newX < 0 or arr[newY][newX] != 0:
            dir_state =(dir_state + 1) % 4
            newX = X + dx[dir_state]
            newY = Y + dy[dir_state]

        num += 1


import sys
sys.stdin = open('달팽이.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]

    solve(arr)

    print("#{}".format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()