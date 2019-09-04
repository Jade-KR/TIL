import sys
sys.stdin = open('파스칼.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            if j > i:
                break
            if j == 0 or j == N-1:
                arr[i][j] = 1
            if 0 < j < N-1 and i > 0:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                print(arr[i][j], end=' ')
        print()