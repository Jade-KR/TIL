import sys
sys.stdin = open('미로.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    tmp = 0
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if not (0<=new_x<N and 0<=new_y<N): #인덱스 벗어나는 것 먼저 조건 걸어줘야함
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

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]



    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                start = i, j
    print('#{} '.format(tc), end="")
    print(dfs(start[1], start[0]))