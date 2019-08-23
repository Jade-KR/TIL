import sys
sys.stdin = open('문자열비교.txt')

T = int(input())
for tc in range(1, T+1):
    N = input()
    M = input()
    cnt = 0

    for i in range(len(M) - len(N) + 1):
        cmp = M[i:len(N)+i]
        if cmp == N:
            cnt += 1

    if cnt:
        cnt = 1

    print('#{} {}'.format(tc, cnt))

