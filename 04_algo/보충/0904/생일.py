import sys
sys.stdin = open('생일.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    rs = [list(map(int, input().split())) for _ in range(M)]
    check = [0]*(M+1)
    cnt = 0
    tmp = [1]

    for i in range(M):
        if rs[i][0] == 1:
            check[rs[i][1]] = 1
            tmp.append(rs[i][1])
        elif rs[i][1] == 1:
            check[rs[i][0]] = 1
            tmp.append(rs[i][0])

    for i in range(M):
        if rs[i][0] in tmp and rs[i][1] in tmp:
            continue

        if rs[i][0] in tmp and rs[i][1] not in tmp:
            check[rs[i][1]] = 1
            continue

        if rs[i][1] in tmp and rs[i][0] not in tmp:
            check[rs[i][0]] = 1
            continue

    for i in check:
        if i == 1:
            cnt += 1

    print('#{} {}'.format(tc, cnt))

    # print('#{} {}'.format(tc, cnt))