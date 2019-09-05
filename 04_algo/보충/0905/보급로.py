def bfs(x, y):
    global sum_d
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = []
    q.append((x, y))
    # visited[x][y] = 1
    while len(q) != 0:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]



import sys
sys.stdin = open('보급로.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    sum_d = 0

    print('#{} {}'.format(tc, bfs(0, 0)))