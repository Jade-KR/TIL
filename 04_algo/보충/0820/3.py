import sys
sys.stdin = open('3.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    value = [list(map(int, input())) for _ in range(N)]

    sum_v = 0
    cnt = 0
    for i in range(N):
        if i == 0:
            sum_v += value[i][N//2]
            cnt += 1
        elif i > 0 and i <= N//2:
            sum_v += sum(value[i][(N//2)-cnt: (N//2)+cnt+1])
            cnt += 1
            if cnt == N//2 + 1:
                cnt -= 2
        elif i > N//2:
            sum_v += sum(value[i][(N//2) - cnt: (N//2)+cnt+1])
            cnt -= 1

    print('#{} {}'.format(tc, sum_v))
    # 중간 변수 만들고, 시작 줄이고 마침 늘리고