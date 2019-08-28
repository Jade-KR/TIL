def perm(n, k, cursum):
    global ans
    if ans < cursum:
        return
    if k == n:
        if ans > cursum: ans = cursum
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1, cursum + data[k][arr[k]])
            arr[k], arr[i] = arr[i], arr[k]


import sys
sys.stdin = open('최소배열의합.txt')


for tc in range(1, T+1):
    ans = 987654321
    N = int(input())
    arr = [0] * N
    for i in range(N):
        arr[i] = i
    data =