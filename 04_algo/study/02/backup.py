import sys
sys.stdin = open("소용돌이.txt")

r1, c1, r2, c2 = map(int, input().split())

# 출력할 범위
a = abs(r1-r2)+1
b = abs(c1-c2)+1

# 판의 최대 크기 만들기
N = 2*(max(abs(r1), abs(r2), abs(c1), abs(c2)))
board = [[0]*(b) for _ in range(a)]
x, y = abs(r1), abs(r1)
max_c = a*b
paint = 0
cnt = 1

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
change = 0
length = 1
check = 0

# 마지막 수부터 1씩 깎으면서 0,0 으로 회오리 그리기
if 0 <= x < a and 0 <= y < b:
    board[x][y] = cnt
    paint += 1
cnt += 1

for i in range(N+1):
    if check == 1:
        break
    for j in range(2):
        if check == 1:
            break
        for k in range(length):
            if check == 1:
                break
            x = x + dx[change%4]
            y = y + dy[change%4]
            if 0 <= x < a and 0 <= y < b:
                board[x][y] = cnt
                paint += 1
                if paint >= max_c:
                    check = 1
            cnt += 1
        change += 1
    length += 1


for i in range(a):
    for j in range(b):
        print(board[i][j], end=' ')
    print()