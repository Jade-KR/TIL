def dfs(y, x, st):
    if len(st) == 7:
        comp.add(st)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            continue
        dfs(ny, nx, st + str(data[nx][ny]))


import sys
sys.stdin = open('격자판.txt')

T = int(input())
for tc in range(1, T+1):
    data = [list(map(int, input().split())) for _ in range(4)]
    comp = set()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        for j in range(4):
            st = str(data[i][j])
            dfs(j, i, st)

    print('#{} {}'.format(tc, len(comp)))