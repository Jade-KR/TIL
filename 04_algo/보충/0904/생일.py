import sys
sys.stdin = open('생일.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    rs = [list(map(int, input().split())) for _ in range(M)]
    check = [0]*(M+1)
    cnt = 0
    tmp = []
    for i in range(M):
        if rs[i][0] == 1:
            tmp.append(rs[i][1])
            check[rs[i][1]] = 1
            cnt += 1

        elif rs[i][1] == 1:
            tmp.append(rs[i][0])
            check[rs[i][0]] = 1
            cnt += 1

    for i in range(M):
        if rs[i][0] in tmp or rs[i][1] in tmp:
            if check[rs[i][0]] != 0 and check[rs[i][1]] != 0:
                cnt += 1

    print('#{} {}'.format(tc, cnt))