import sys
sys.stdin = open('보물상자.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    pw = input()
    rg = N // 4
    cnt = 0
    each = ''
    tmp = []

    while cnt < N//4:
        for i in range(0, len(pw), N//4):
            for j in range(N // 4):
                each += pw[i+j]
            if each not in tmp:
                tmp.append(each)
            each = ''
        pw = pw[-1] + pw[0:-1]
        cnt += 1

    for i in range(len(tmp)):
        tmp[i] = int(tmp[i], 16)

    result = sorted(tmp)

    print('#{} {}'.format(tc, result[-K]))





