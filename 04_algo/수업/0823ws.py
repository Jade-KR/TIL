import sys
sys.stdin = open('0820ws.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    tmp = 0
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if not (0<=new_x<16 and 0<=new_y<16):
            continue

        if data[new_y][new_x] == 3:
            return 1

        if visited[new_y][new_x] != 0 or data[new_y][new_x] > 0:
            continue
        visited[new_y][new_x] = 1
        tmp = dfs(new_x, new_y)
        if tmp:
            break
    return tmp


T = 10
for tc in range(1, T+1):
    n = int(input())
    data = [list(map(int, input())) for _ in range(16)]
    visited = [[0 for _ in range(16)] for i in range(16)]

    for i in range(16):
        for j in range(16):
            if data[i][j] == 2:
                start = [i, j]
            if data[i][j] == 3:
                goal = [i, j]

    print('#{}'.format(tc), end=" ")
    print(dfs(start[1], start[0]))

