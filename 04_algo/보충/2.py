import sys
sys.stdin = open('2.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    max_d = 0
    data = [list(map(int, input().split())) for _ in range(N)]
    tmp = []
    sum_d = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_d = 0
            for x in range(M):
                for y in range(M):
                    sum_d += data[i+x][j+y]


            if max_d < sum_d:
                max_d = sum_d

    print('#{} {}'.format(tc, max_d))
