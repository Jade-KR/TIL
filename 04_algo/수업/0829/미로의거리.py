dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    newX, newY = x, y





import sys
sys.stdin = open('미로의거리.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = [j, i]

    bfs(start[0], start[1])