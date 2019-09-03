def perm(n, k, cur):
    global ans
    if ans >= cur:
        return
    if k == n:
        if ans < cur:
            ans = cur
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1, cur*0.01*data[k][arr[k]-1])
            arr[k], arr[i] = arr[i], arr[k]

import sys
sys.stdin = open('동철.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    arr = [i+1 for i in range(N)]
    perm(N, 0, 100)

    print('#%d %.6f' % (tc, ans))