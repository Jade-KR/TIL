import sys
sys.stdin = open('농작물.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    mid = N // 2
    sum_f = 0
    cnt = 0

    for i in range(N):
        if i == 0:
            sum_f += farm[i][mid]
            cnt += 1
        elif 0 < i <= mid:
            sum_f += sum(farm[i][mid - cnt: mid + cnt + 1])
            cnt += 1
            if cnt == mid + 1:
                cnt -= 2
        elif i > mid:
            sum_f += sum(farm[i][mid - cnt: mid + cnt + 1])
            cnt -= 1

    print('#{} {}'.format(tc, sum_f))





