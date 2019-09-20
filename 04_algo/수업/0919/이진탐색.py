def binsearch(l, r, m, b):
    global cnt, flag, result, left, right
    if flag == 1:
        return
    m = (l+r)//2

    if a[m] < b:
        l = m+1
        right += 1
    elif a[m] > b:
        r = m-1
        left += 1
    elif a[m] == b:
        flag = 1
        if left > right+1 or right > left+1:
            return
        cnt += 1
    if l > r:
        flag = 1
        return
    binsearch(l, r, m, b)


import sys
sys.stdin = open('이진탐색.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    B = list(map(int, input().split()))
    l = 0
    r = len(a)-1
    m = (l+r)//2
    result = 0
    left = 0
    right = 0
    for i in B:
        flag = 0
        cnt = 0
        left, right = 0, 0
        binsearch(l, r, m, i)
        result += cnt

    print('#{} {}'.format(tc, result))