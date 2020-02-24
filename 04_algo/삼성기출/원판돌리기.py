import sys
sys.stdin = open('원판돌리기.txt')
import collections

def rotation(a, b, c):
    arr = []
    for i in range(1, N+1):
        if i % a == 0:
            arr.append(i-1)

    for i in arr:
        if b == 0:
            for _ in range(c):
                t = board[i].pop()
                board[i].insert(0, t)
        else:
            for _ in range(c):
                t = board[i].popleft()
                board[i].append(t)

def checkSame(x, y):
    q = collections.deque()
    q.append((x, y))
    while len(q):
        x, y = q.popleft()
        if y == 0:
            if board[x][y] == board[x][y-1]:
                check[x][y], check[x][y-1] = 1, 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if board[x][y] == board[nx][ny]:
                    check[x][y], check[nx][ny] = 1, 1


def setBoard():
    chk = 0
    for i in range(N):
        for j in range(M):
            if check[i][j] == 1:
                chk = 1
                board[i][j] = 0

    if chk == 0:
        tmp = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                tmp += board[i][j]
                if board[i][j] != 0:
                    cnt += 1

        if cnt != 0:
            avg = tmp / cnt
            for i in range(N):
                for j in range(M):
                    if board[i][j] < avg and board[i][j]:
                        board[i][j] += 1
                    elif board[i][j] > avg and board[i][j]:
                        board[i][j] -= 1

N, M, T = map(int, input().split())
board = [collections.deque((map(int, input().split()))) for _ in range(N)]
dare = [list(map(int, input().split())) for _ in range(T)]
ans = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for a in range(T):
    check = [[0]*M for _ in range(N)]
    x, d, k = dare[a]
    rotation(x, d, k)
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                checkSame(i, j)
    setBoard()

for i in range(N):
    for j in range(M):
        ans += board[i][j]

print(ans)