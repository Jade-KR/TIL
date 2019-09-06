def perm2(arr=[]):
    global sum_d
    if len(arr) == 3:
        for i in range(3):
            sum_d *= data[i][arr[i]] / 100
        tmp.append(sum_d * 100)

        return
    for i in range(3):
        if not vl[i]:
            arr.append(i)
            vl[i]=1
            perm2(arr)
            arr.pop()
            vl[i]=0

import sys
sys.stdin = open('동철.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    sum_d = 1
    tmp = []
    vl = [0, 0, 0]
    perm2()
    print(tmp)
