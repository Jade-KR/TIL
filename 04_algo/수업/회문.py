import sys
sys.stdin = open('회문.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    box = []
    p = ''
    for i in range(N):
        box.append(input())

    for i in range(N):
        for j in range(N - M + 1):
            cmp = box[i][j:j + M]
            if cmp == cmp[::-1]:
                p = cmp

    for i in range(N - M +1):
        for j in range(N):
            cmp = ''
            for k in range(M):
                cmp += box[i + k][j]
            if cmp == cmp[::-1]:
                p = cmp
    print('#{} {}'.format(tc, p))