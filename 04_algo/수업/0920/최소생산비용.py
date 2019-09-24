def perm(arr=[], cur):
    global sum_v, cnt, min_v
    if len(arr) == N:
        cnt = 0
        sum_v = 0
        while cnt < N:
            sum_v += V[cnt][arr[cnt]]
            cnt += 1
        if min_v > sum_v:
            min_v = sum_v
    for i in range(N):
        if not vl[i]:
            arr.append(i)
            vl[i] = 1
            perm(arr)
            arr.pop()
            vl[i] = 0

import sys
sys.stdin = open('최소생산비용.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    vl = [0]*N
    arr = []
    cnt = 0
    min_v = 987654321
    s = 0
    perm(arr, 0)

    print('#{} {}'.format(tc, min_v))