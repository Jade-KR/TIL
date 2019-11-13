import sys
sys.stdin = open('연산.txt')

def perm(dep, ans):
    global min_n, max_n
    if dep == N-1:
        if min_n > ans:
            min_n = ans
        if max_n < ans:
            max_n = ans
    else:
        if cnt_cal[0] > 0:
            cnt_cal[0] -= 1
            perm(dep+1, ans + numbers[dep+1])
            cnt_cal[0] += 1

        if cnt_cal[1] > 0:
            cnt_cal[1] -= 1
            perm(dep+1, ans - numbers[dep+1])
            cnt_cal[1] += 1

        if cnt_cal[2] > 0:
            cnt_cal[2] -= 1
            perm(dep+1, ans * numbers[dep+1])
            cnt_cal[2] += 1

        if cnt_cal[3] > 0:
            cnt_cal[3] -= 1
            perm(dep+1, int(ans / numbers[dep+1]))
            cnt_cal[3] += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt_cal = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    min_n = 987987
    max_n = -5616519

    perm(0, numbers[0])

    print('#{} {}'.format(tc, (max_n - min_n)))