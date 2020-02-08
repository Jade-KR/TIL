import sys
sys.stdin = open("뱀.txt")
import collections

def location(v):
    global nx, ny
    if v == 0: #북쪽.
        nx -= 1
    elif v == 1: #동쪽.
        ny += 1
    elif v == 2:
        nx += 1 # 남쪽.
    elif v == 3:
        ny -= 1 # 서쪽.


N = int(input())
K = int(input())
apple = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
directionInfo = [list(map(str, input().split())) for _ in range(L)]
board = [[0]*N for _ in range(N)]
checkDirection = [0]*10001
check = 0
k = 0
x, y = 0, 0
d = 1
nx, ny = 0, 0
dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]
tail = collections.deque()

for i in range(K):
    board[apple[i][0]-1][apple[i][1]-1] = 2

for j in range(L):
    checkDirection[int(directionInfo[j][0])] = directionInfo[j][1]


while check == 0:
    chk = 0
    if checkDirection[k] == 'L':
        if d > 0:
            d = d - 1
        else:
            d = 3

    elif checkDirection[k] == 'D':
        if d < 3:
            d = d + 1
        else:
            d = 0
    location(d)
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        break
    if (x, y) not in tail:
        tail.append((x, y))

    if board[nx][ny] == 0:
        x, y = nx, ny
        board[nx][ny] = 1

    elif board[nx][ny] == 1:
        break

    elif board[nx][ny] == 2:
        board[x][y] = 1
        board[nx][ny] = 1
        x, y = nx, ny
        chk = 1

    if chk == 0:
        tx, ty = tail.popleft()
        board[tx][ty] = 0

    k += 1

print(k+1)