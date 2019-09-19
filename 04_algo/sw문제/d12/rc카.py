import sys
sys.stdin = open('rc카.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    d = 0
    s = 0

    for i in range(N):
        if data[i][0] == 1:
            s += data[i][1]
            d += s
        elif data[i][0] == 2:
            if data[i][1] >= s:
                s = 0
                d += s
            else:
                s -= data[i][1]
                d += s
        elif data[i][0] == 0:
            d += s

    print('#{} {}'.format(tc, d))