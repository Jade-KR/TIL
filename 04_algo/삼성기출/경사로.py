import sys
sys.stdin = open('경사로.txt')


def checkBack(x, y, v):
    global flag
    a, b = x, y
    chk = 0
    for _ in range(L):
        if 0 <= b < N and 0 <= a < N:
            if check[a][b] != 1 and ladder[a][b] == v:
                b -= 1
            else:
                chk = 1
        else:
            chk = 1
            break
    b += 1
    if chk == 0:
        for _ in range(L):
            check[a][b] = 1
            b += 1
    else:
        flag = 1

def checkFront(x, y, v):
    global flag
    a, b = x, y
    chk = 0
    for _ in range(L):
        if 0 <= b < N and 0 <= a < N:
            if check[a][b] != 1 and ladder[a][b] == v:
                b += 1
            else:
                chk = 1
        else:
            chk = 1
            break
    b -= 1
    if chk == 0:
        for _ in range(L):
            check[a][b] = 1
            b -= 1
    else:
        flag = 1

def checkTop(x, y, v):
    global flag
    a, b = x, y
    chk = 0
    for _ in range(L):
        if 0 <= b < N and 0 <= a < N:
            if check[a][b] != 1 and ladder[a][b] == v:
                a -= 1
            else:
                chk = 1
        else:
            chk = 1
            break
    a += 1
    if chk == 0:
        for _ in range(L):
            check[a][b] = 1
            a += 1
    else:
        flag = 1

def checkBottom(x, y, v):
    global flag
    a, b = x, y
    chk = 0
    for _ in range(L):
        if 0 <= b < N and 0 <= a < N:
            if check[a][b] != 1 and ladder[a][b] == v:
                a += 1
            else:
                chk = 1
        else:
            chk = 1
            break
    a -= 1
    if chk == 0:
        for _ in range(L):
            check[a][b] = 1
            a -= 1
    else:
        flag = 1

N, L = map(int, input().split())
ladder = [list(map(int, input().split())) for _ in range(N)]
check = [[0]*N for _ in range(N)]
cnt = 0
ans = 0

# 가로 길 체크
for i in range(N):
    chk = 0
    flag = 0
    for j in range(N-1):
        if abs(ladder[i][j] - ladder[i][j+1]) > 1:
            cnt += 1
            break

        if ladder[i][j] == ladder[i][j+1]:
            continue

        if ladder[i][j] != ladder[i][j+1]:
            if ladder[i][j] < ladder[i][j+1]:
                checkBack(i, j, ladder[i][j])
                if flag == 1:
                    cnt += 1
                    break
            else:
                checkFront(i, j+1, ladder[i][j+1])
                if flag == 1:
                    cnt += 1
                    break

check = [[0]*N for _ in range(N)]
# 세로 길 체크
for j in range(N):
    chk = 0
    flag = 0
    for i in range(N-1):
        if abs(ladder[i][j] - ladder[i+1][j]) > 1:
            cnt += 1
            break

        if ladder[i][j] == ladder[i+1][j]:
            continue

        if ladder[i][j] != ladder[i+1][j]:
            if ladder[i][j] < ladder[i+1][j]:
                checkTop(i, j, ladder[i][j])
                if flag == 1:
                    cnt += 1
                    break
            else:
                checkBottom(i+1, j, ladder[i+1][j])
                if flag == 1:
                    cnt += 1
                    break


ans = 2*N - cnt

print(ans)








