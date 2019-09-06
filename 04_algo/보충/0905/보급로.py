import sys
sys.stdin = open('보급로.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    print('#{} {}'.format(tc, bfs(0, 0)))