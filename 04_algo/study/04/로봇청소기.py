import sys

sys.stdin = open('로봇청소기.txt')


def setDirection(v):
    if v == 0:
        return 3
    else:
        return v - 1

def setWay(height, width, direction):
    global newHeight, newWidth
    if direction == 0:
        newHeight = height - 1
        newWidth = width
    elif direction == 1:
        newHeight = height
        newWidth = width + 1
    elif direction == 2:
        newHeight = height + 1
        newWidth = width
    elif direction == 3:
        newHeight = height
        newWidth = width - 1


def back(height, width, direction):
    global newHeight, newWidth, finish
    if direction == 0:
        newHeight = height+1
        newWidth = width
    elif direction == 1:
        newHeight = height
        newWidth = width-1
    elif direction == 2:
        newHeight = height-1
        newWidth = width
    elif direction == 3:
        newHeight = height
        newWidth = width+1

    if newHeight < 0 or newHeight >= N or newWidth < 0 or newWidth >= M or floor[newHeight][newWidth] == 1:
        finish = 1

def active(height, width, direction):
    global r, c, d, changed
    if 0 <= height < N and 0 <= width < M:
        if visited[height][width] == 0 and floor[height][width] == 0:
            r = height
            c = width
            changed = 1
            return
        else:
            d = direction
            return
    else:
        d = direction
        return

N, M = map(int, input().split())
r, c, d = map(int, input().split())
floor = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
finish = 0
cleaned = 0
newHeight = 0
newWidth = 0
# 0 = 북, 1 = 동, 2 = 남, 3 = 서
while finish == 0:
    changed = 0
    visited[r][c] = 1
    for a in range(4):
        # 방향 설정.
        d = setDirection(d)
        # 왼쪽 방향 보기.
        setWay(r, c, d)
        # 청소 시작.
        active(newHeight, newWidth, d)
        # 청소가 됐으면 다시 처음부터.
        if changed == 1:
            break
        # 청소 실패했으면.
    if changed == 0:
        # 방향을 유지하고 2칸 후진.
        back(r, c, d)
        r = newHeight
        c = newWidth

# 청소한 곳 탐색.
for i in range(N):
    for j in range(M):
        if visited[i][j] == 1:
            cleaned += 1
print(cleaned)