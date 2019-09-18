def perm(arr=[]):
    global min_d
    if len(arr) == N and arr[0] == 0:
        sum_d = 0
        for k in range(len(arr)):
            if k == len(arr)-1:
                sum_d += data[arr[k]][0]
            else:
                sum_d += data[arr[k]][arr[k+1]]
        if min_d > sum_d:
            min_d = sum_d

    for i in range(N):
        if not vl[i]:
            arr.append(i)
            if arr[0] != 0:
                return
            vl[i] = 1
            perm(arr)
            arr.pop()
            vl[i] = 0


import sys
sys.stdin = open('전자키트.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    vl = [0]*N
    arr = []
    sum_d = 0
    min_d = 987654321
    perm(arr)

    print('#{} {}'.format(tc, min_d))