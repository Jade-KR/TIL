import sys
import collections
sys.stdin = open('방범서비스.txt')

def bfs(x, y):
    q = collections.deque()
    visited[x][y] = 1
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for w in range(4):
            nx = x + dx[w]
            ny = y + dy[w]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] != 0:
                continue
            if visited[x][y] < K:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
            else:
                pass

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    K = 1
    cnt = 0
    cost = 0
    money = 0
    house = 0
    result = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                cnt += M

    while cost <= cnt:
        K += 1
        cost = K * K + (K - 1) * (K - 1)
        if cost >= cnt:
            K -= 1
            cost = K * K + (K - 1) * (K - 1)
            break

    while result == 0:
        for i in range(N):
            for j in range(N):
                visited = [[0] * N for _ in range(N)]
                bfs(i, j)
                money = 0
                for z in range(N):
                    for c in range(N):
                        if visited[z][c]:
                            if data[z][c] == 1:
                                money += M
                if cost <= money:
                    house = money // M
                if result < house:
                    result = house
        K -= 1
        cost = K * K + (K - 1) * (K - 1)
    print('#{} {}'.format(tc, result))