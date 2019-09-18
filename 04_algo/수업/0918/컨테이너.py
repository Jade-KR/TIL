import sys
sys.stdin = open('컨테이너.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    C = list(map(int, input().split()))
    sw = sorted(W)
    sc = sorted(C)
    sum_w = 0

    for j in sc:
        for i in range(len(sw)-1, -1, -1):
            if j >= sw[i]:
                sum_w += sw[i]
                sw[i] = 987654321
                break

    print('#{} {}'.format(tc, sum_w))