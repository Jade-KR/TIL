import sys
sys.stdin = open('성적.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    val = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    score = [0]

    for i in range(N):
        sum_a = 0
        sum_a += arr[i][0]*35 + arr[i][1]*45 + arr[i][2]*20
        score.append(sum_a)
    cnt = 0
    for j in score:
        if score[K] < j:
            cnt += 1

    print('#{} {}'.format(tc, val[cnt//(N//10)]))