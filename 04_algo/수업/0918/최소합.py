dx = [1, 0]
dy = [0, 1]
def dfs(x, y, s):
    global min_d
    if s > min_d:
        return
    s += data[y][x]
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if nx == N-1 and ny == N-1:
            s += data[ny][nx]
            if s < min_d:
                min_d = s
            return
        dfs(nx, ny, s)




import sys
sys.stdin = open('최소합.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    x, y = 0, 0
    s = 0
    min_d = 98765421
    dfs(y, x, s)


    print('#{} {}'.format(tc, min_d))