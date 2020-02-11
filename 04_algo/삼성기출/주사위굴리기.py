import sys
sys.stdin = open("주사위굴리기.txt")
import collections

def setDirection(v):
    global nx, ny
    if v == 1:
        ny = y+1
        nx = x
    elif v == 2:
        ny = y-1
        nx = x
    elif v == 3:
        ny = y
        nx = x-1
    elif v == 4:
        ny = y
        nx = x+1

def setDice(v):
    if v == 1:
        t = diceX.pop()
        diceX.insert(0, t)
        diceY[0] = diceX[0]
        diceY[2] = diceX[2]

    elif v == 2:
        t = diceX.popleft()
        diceX.append(t)
        diceY[0] = diceX[0]
        diceY[2] = diceX[2]

    elif v == 3:
        t = diceY.popleft()
        diceY.append(t)
        diceX[0] = diceY[0]
        diceX[2] = diceY[2]

    elif v == 4:
        t = diceY.pop()
        diceY.insert(0, t)
        diceX[0] = diceY[0]
        diceX[2] = diceY[2]

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
order = collections.deque(list(map(int, input().split())))

diceX = collections.deque([0]*4)
diceY = collections.deque([0]*4)

# diceX = 윗, 오른, 아래, 왼
# diceY = 윗, 앞, 아래, 뒤

# 동쪽 1 - diceX - pop() > insert(0, t), diceY - 윗면 = diceX[0]
# 서쪽 2 - diceX - pop(0) > append(t), diceY - 윗면 = diceX[0]
# 북쪽 3 - diceY - pop(0) > append(t), diceX - 윗면 = diceY[0]
# 남쪽 4 - diceY - pop() > insert(0, t), diceX - 윗면 = diceY[0]


while len(order):
    go = order.popleft()
    setDirection(go)
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
    #굴린다.
    setDice(go)

    if board[nx][ny] != 0:
        diceX[2] = board[nx][ny]
        diceY[2] = board[nx][ny]
        board[nx][ny] = 0
    else:
        board[nx][ny] = diceX[2]

    print(diceX[0])
    x, y = nx, ny