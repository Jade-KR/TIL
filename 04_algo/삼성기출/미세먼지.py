import sys
sys.stdin = open('미세먼지.txt')

def diffusion(x, y):
    chk = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or nx >= R or ny < 0 or ny >= C or room[nx][ny] == -1:
            continue
        chk += 1
        tmp[nx][ny] = tmp[nx][ny] + room[x][y]//5
    room[x][y] = room[x][y] - (room[x][y]//5) * chk

def activeUp(x, y):
    global room
    ox, oy = x, y
    k = 0
    chk = 0
    while chk == 0:
        nx = x + ucx[k]
        ny = y + ucy[k]
        if nx < 0 or nx >= R or ny < 0 or ny >= C or nx > ox:
            k += 1
            k = k%4
            continue
        if room[nx][ny] == -1:
            chk = 1
            break
        if nx == ox-1 and ny == oy:
            room[nx][ny] = 0
            x, y = nx, ny
            continue
        room[x][y] = room[nx][ny]
        room[nx][ny] = 0
        x, y = nx, ny

def activeDown(x, y):
    global room
    ox, oy = x, y
    k = 0
    chk = 0
    while chk == 0:
        nx = x + dcx[k]
        ny = y + dcy[k]
        if nx < 0 or nx >= R or ny < 0 or ny >= C or nx < ox:
            k += 1
            k = k % 4
            continue
        if room[nx][ny] == -1:
            chk = 1
            break
        if nx == ox+1 and ny == oy:
            room[nx][ny] = 0
            x, y = nx, ny
            continue
        room[x][y] = room[nx][ny]
        room[nx][ny] = 0
        x, y = nx, ny

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
cleaner = []
ans = 0

ucx = [-1, 0, 1, 0]
ucy = [0, 1, 0, -1]

dcx = [1, 0, -1, 0]
dcy = [0, 1, 0, -1]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 확산 -> 공기청정

for i in range(R):
    if room[i][0] == -1:
        cleaner.append(i)

while T > 0:
    tmp = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if room[i][j] >= 5:
                diffusion(i, j)

    for i in range(R):
        for j in range(C):
            if room[i][j] != -1:
                room[i][j] = room[i][j] + tmp[i][j]

    activeUp(cleaner[0], 0)
    activeDown(cleaner[1], 0)

    T -= 1

for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            ans += room[i][j]

print(ans)