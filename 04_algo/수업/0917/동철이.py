# def perm(d=0, s=1):
#     global sum_d, r
#     if d == N:
#         for j in range(len(d)):
#             sum_d *= data[j][d[j]] / 100
#         tmp.append(sum_d * 100)
#         return
#
#     for i in range(N):
#         if not A[i]:
#             A[i] = 1
#             perm(d+1, s*data[d][i])
#             A[i] = 0
#
#
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     A = [0 for _ in range(N)]
#     sum_d = 1
#     r = 0
#     tmp = []
#     perm()
#     print('#{} '.format(tc), end="")
#     print('%f' % max(tmp))


def perm(d = 0, s = 1):
    global r
    if d == N:
        if s > r:
            r = s
        return
    if s <= r:
        return

    for i in range(N):
        if not vl[i]:
            vl[i] = 1
            perm(d+1, s*data[d][i])
            vl[i] = 0

import sys
sys.stdin = open('동철이.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    data = [[0.01*i for i in list(map(int, input().split()))] for _ in range(N)]
    vl = [0]*N
    r = 0
    perm()
    print('#{} {:6f}'.format(t, r*100))