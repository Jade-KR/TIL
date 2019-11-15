import sys
sys.stdin = open('디저트카페.txt')
import collections

def dfs(x, y):
    global ans, flag
    if flag == 1:
        return
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if visited[x][y] != 1:
            if nx == s and ny == e:
                flag = 1
                if ans < visited[x][y] + 1:
                    ans = visited[x][y] + 1
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if visited[nx][ny]: continue
        if cafe[nx][ny] in dessert:
            continue
        visited[nx][ny] += visited[x][y] + 1
        dessert.append(cafe[nx][ny])
        dfs(nx, ny)
        dessert.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, 1]
    ans = 0
    visited = [[0] * N for _ in range(N)]


    for i in range(N-2):
        for j in range(1, N-1):
            dessert = []
            visited = [[0] * N for _ in range(N)]
            s = i
            e = j
            flag = 0
            dessert.append(cafe[i][j])
            dfs(i, j)
    if ans == 0:
        ans = -1
    print('#{} {}'.format(tc, ans))
