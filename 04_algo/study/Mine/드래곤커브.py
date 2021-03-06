import sys
sys.stdin = open("드래곤커브.txt")

def dragon(d, g):
    way = [d]
    for a in range(g):
        for b in range(len(way)-1, -1, -1):
            way.append((way[b] + 1) % 4)

    for k in way:
        if k == 0:
            point.append([point[-1][0] + 1, point[-1][1]])

        elif k == 1:
            point.append([point[-1][0], point[-1][1] - 1])

        elif k == 2:
            point.append([point[-1][0] - 1, point[-1][1]])

        elif k == 3:
            point.append([point[-1][0], point[-1][1] + 1])

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
board = [[0]*101 for _ in range(101)]
point = []
cnt = 0

for i in range(N):
    point.append([info[i][0], info[i][1]])
    dragon(info[i][2], info[i][3])

for k in range(len(point)):
    board[point[k][1]][point[k][0]] = 1


for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            if board[i][j+1] == 1 and board[i+1][j] == 1 and board[i+1][j+1] == 1:
                cnt += 1
print(cnt)
