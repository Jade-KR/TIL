import sys
sys.stdin = open('회전.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    Q = []

    for j in data:
        Q.append(j)

    for i in range(M):
        Q.append(Q.pop(0))

    print('#{} {}'.format(tc, Q[0]))

