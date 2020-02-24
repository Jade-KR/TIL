import sys
sys.stdin = open('이차원배열과연산.txt')

def checkR():
    global max_c, flag
    chk = 0
    max_c = 0
    while chk <= R:
        tmp = []
        amount = [0] * 101
        for k in range(C):
            if board[chk][k] != 0:
                amount[board[chk][k]] += 1
        for c in range(1, 101):
            for k in range(1, 101):
                if amount[k] == c:
                    tmp.append(k)
                    tmp.append(amount[k])

        if max_c < len(tmp):
            max_c = len(tmp)

        for i in range(101):
            if i < len(tmp):
                board[chk][i] = tmp[i]
            else:
                board[chk][i] = 0

        if max_c > 100:
            break

        chk += 1

def checkC():
    global max_r, flag
    chk = 0
    max_r = 0
    while chk <= C:
        tmp = []
        amount = [0] * 101
        for k in range(R):
            if board[k][chk] != 0:
                amount[board[k][chk]] += 1
        for c in range(1, 101):
            for k in range(1, 101):
                if amount[k] == c:
                    tmp.append(k)
                    tmp.append(amount[k])

        if max_r < len(tmp):
            max_r = len(tmp)

        for i in range(101):
            if i < len(tmp):
                board[i][chk] = tmp[i]
            else:
                board[i][chk] = 0

        if max_r > 100:
            break

        chk += 1

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
board = [[0]*102 for _ in range(102)]
flag = 0
max_c = 3
max_r = 3
for i in range(3):
    for j in range(3):
        board[i][j] = A[i][j]
t = 0
check = 0
R = 3
C = 3

while t < 101 and check == 0:
    if board[r-1][c-1] == k:
        check = 1
        break

    if R >= C:
        checkR()
    else:
        checkC()

    R = max_r
    C = max_c

    if R > 100:
        R = 100

    if C > 100:
        C = 100

    t += 1

if t > 100:
    print(-1)
else:
    print(t)