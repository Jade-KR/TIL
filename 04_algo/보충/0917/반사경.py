import sys
sys.stdin = open('반사경.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    x, y = 0, 0

    while 1:
        x += 1
        if x < 0 or x >= N or y < 0 or y >= N:
            break
