def clear(data):


def work(data):
    if S == 'up':
        for i in range(N-1):
            for j in range(N):
                cnt = 1
                while True:
                    if data[i][j] == data[i+cnt][j]:
                        data[i][j] *= 2
                        cnt += 1


                        # if i < N-2:
                        #     data[i+1][j] = data[i+2][j]
                        #     if data[i+2][j] == 0:
                        #
                        #
                        # if i == N-2:
                        #     data[i]





import sys
sys.stdin = open('2048.txt')

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc))
    n, S = input().split()
    N = int(n)
    data = [list(map(int, input().split())) for _ in range(N)]

    work(data)

    for i in range(N):
        for j in range(N):
            print(data[i][j], end=' ')
        print()