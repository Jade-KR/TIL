def dfs(x, y):
    global n, min_x, min_y, max_x, max_y
    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n:
            continue

        if visited[new_y][new_x] != 0 or data[new_y][new_x] == 0:
            continue

        visited[new_y][new_x] = 1

        dfs(new_x, new_y)

import sys
sys.stdin = open('행렬찾기.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    result = []
    cmp = []

    for i in range(n):
        for j in range(n):
            if data[i][j] != 0 and visited[i][j] == 0:
                min_x, min_y, max_x, max_y = n, n, 0, 0
                dfs(j, i)
                width = max_y - min_y + 1
                height = max_x - min_x + 1
                size = width*height
                result.append((width, height))
                cmp.append(width*height)
                cnt += 1




    for i in range(len(cmp)-1):
        if cmp[i] > cmp[i+1]:
            cmp[i], cmp[i+1] = cmp[i+1], cmp[i]
            result[i], result[i+1] = result[i+1], result[i]
        if cmp[i] == cmp[i+1]:
            if result[i][0] > result[i+1][0]:
                result[i], result[i+1] = result[i+1], result[i]

    print(result)

    # final = []
    #
    # print('#{} {}'.format(tc, cnt), end=" ")
    # for k in result:
    #     for l in range(2):
    #         final.append(k[l])
    #
    # for k in final:
    #     print(k, end=" ")
    # print()