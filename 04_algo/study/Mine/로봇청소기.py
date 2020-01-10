import sys
sys.stdin = open('로봇청소기.txt')
def setDirection(v):
    if v == 0:
        return 4
    else:
        return v-1

def active(height, width, direction):
    visited[height][width] = 1
    newDirection = setDirection(direction)
    if newDirection == 0:
        newHeight = height-1
        newWidth = width
    elif newDirection == 1:
        newHeight = height
        newWidth = width+1
    elif newDirection == 2:
        newHeight = height+1
        newWidth = width
    elif newDirection == 3:
        newHeight = height
        newWidth = width-1

    if 0 <= newHeight < N and 0 <= newWidth < M:
        if visited[newHeight][newWidth] == 0 and floor[newHeight][newWidth] == 0:
            active(newHeight, newWidth, newDirection)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
floor = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]


# 0 = 북, 1 = 동, 2 = 남, 3 = 서
active(r, c, d)
