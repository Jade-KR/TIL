import sys
sys.stdin = open('파리잡기.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_a = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
                sum_a = 0
                for x in range(M):
                    for y in range(M):
                        sum_a += arr[x+i][y+j]
                if max_a < sum_a:
                    max_a = sum_a

    print('#{} {}'.format(tc, max_a))