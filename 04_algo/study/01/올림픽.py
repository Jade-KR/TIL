import sys
sys.stdin = open('올림픽.txt')

N, K = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
rank = 0

for k in range(N):
    if info[k][0] == K:
        A = k

for i in range(N):
    if info[i][1] > info[A][1]:
        rank += 1
    elif info[i][1] == info[A][1]:
        if info[i][2] > info[A][2]:
            rank += 1
        elif info[i][2] == info[A][2]:
            if info[i][3] > info[A][3]:
                rank += 1

print(rank+1)