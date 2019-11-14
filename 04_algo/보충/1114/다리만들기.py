import sys
sys.stdin = open('다리만들기.txt')

def point(x, y):
    for i in range(4):
        cnt = 0
        nx = x + dx[i]
        ny = y + dy[i]
        if data[nx][ny] == 1:
            return
        else:
            while data[x][y] == 1:





N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
# point 체크 가로 세로 ( 같은 숫자, 거리 2 미만 예외처리)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    for j in range(M):
        if data[i][j]:
            point(i, j)

