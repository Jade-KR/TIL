import sys
sys.stdin = open('화물도크.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    shift = [list(map(int, input().split())) for _ in range(N)]
    check = 0
    cnt = 1
    flag = 0

    while check < N:
        for i in range(N-1):
            if shift[i][1] > shift[i+1][1]:
                shift[i], shift[i+1] = shift[i+1], shift[i]
        check += 1

    for i in range(N-1):
        if shift[i+1][0] >= shift[flag][1]:
            flag = i+1
            cnt += 1

    print('#{} {}'.format(tc, cnt))