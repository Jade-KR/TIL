import sys
sys.stdin = open("소용돌이.txt")

r1, c1, r2, c2 = map(int, input().split())

# 출력할 범위
a = abs(r1-r2)+1
b = abs(c1-c2)+1

# 판의 최대 크기 만들기
N = 2*(max(abs(r1), abs(r2), abs(c1), abs(c2)))
board = [[0]*(N+1) for _ in range(N+1)]


x, y = N, N
cnt = (N+1)**2

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
change = 0

# 마지막 수부터 1씩 깎으면서 0,0 으로 회오리 그리기
while cnt > 0:
    if 0 <= a <= 49 and 0 <= b <= 4:
        board[x][y] = cnt

    nx = x + dx[change % 4]
    ny = y + dy[change % 4]

    if nx < 0 or nx >= N+1 or ny < 0 or ny >= N+1:
        change += 1
    elif board[nx][ny]:
        change += 1

    x = x + dx[change % 4]
    y = y + dy[change % 4]
    cnt -= 1

for i in range(a):
    for j in range(b):
        print(board[i][j], end=' ')
    print()

