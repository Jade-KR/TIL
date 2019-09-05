import sys
sys.stdin = open('숫자배열회전.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(4)]


    arr[0] = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1, 4):
        for j in range(N):
            for k in range(N):
                arr[i][k][N-1-j] = arr[i-1][j][k]


    #면, 행, 열
    print('#{}'.format(tc))
    for j in range(N):
        for i in range(1, 4):
            for k in range(N):
                print(arr[i][j][k], end="")
            print(" ", end="")
        print()


