def dfs(x, y):
    global flag
    for i in range(3):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if flag == 1:
            return

        if new_x < 0 or new_x >= 100 or new_y < 0 or new_y >= 100:
            continue

        if visited[new_y][new_x] != 0 or maze[new_y][new_x] == 0:
            continue

        visited[new_y][new_x] = visited[y][x] + 1
        if new_y == 99 and maze[new_y][x] == 1:
            tmp.append(visited[new_y][new_x] - 1)
            flag = 1
            break

        dfs(new_x, new_y)

import sys
sys.stdin = open('ladder.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input().split())) for _ in range(100)]
    s_x = []
    tmp = []
    dx = [1, -1, 0]
    dy = [0, 0, 1]

    for i in range(1):
        for j in range(100):
            if maze[i][j] == 1:
                visited = [[0 for _ in range(100)] for _ in range(100)]
                visited[i][j] = 1
                s_x.append(j)
                flag = 0
                dfs(j, i)


    print('#{} {}'.format(tc, s_x[tmp.index(min(tmp))]))