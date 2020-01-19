import sys
sys.stdin = open("소용돌이.txt")


r1, c1, r2, c2 = map(int, input().split())
positivePoint = [0]*5002
positivePoint[0] = 1
for i in range(5001):
    positivePoint[i+1] = positivePoint[i] + i*8

positivePoint.pop(0)
# 출력할 범위
a = abs(r1-r2)+1
b = abs(c1-c2)+1
board = [[0]*b for _ in range(a)]
length = 1


for i in range(a):
    for k in range(b):
        ni = r1+i
        nk = c1+k
        point = max(abs(ni), abs(nk))
        # ni, nk 절대값 중 큰값을 골라서 Point 찾는다.
        # ni 값이 Point와 같은 값이고 양수일때는 point값에써 nk와 point의 차이만큼  뺀 값
        # nk 값이 point와 같은 값이고 음수일때는 point값-(point*2) 에서 ni와 point의 차이만큼 뺀 값
        # ni 값이 point와 같은 값이고 음수일때는 point값-(point*2)*2 에서 nk와 point의 합만큼 뺀 값
        # nk 값이 point와 같은 값이고 양수일대는 point값-(point*2)*3 에서 ni 와 point의 합만큼 뺀 값
        if ni == point:
            board[i][k] = positivePoint[point] - (point-nk)
            if length < len(str(board[i][k])):
                length = len(str(board[i][k]))
        elif -ni == point:
            board[i][k] = (positivePoint[point]-(point*2)*2) - (point+nk)
            if length < len(str(board[i][k])):
                length = len(str(board[i][k]))
        elif -nk == point:
            board[i][k] = (positivePoint[point]-(point*2)) - (point-ni)
            if length < len(str(board[i][k])):
                length = len(str(board[i][k]))
        elif nk == point:
            board[i][k] = (positivePoint[point]-((point*2)*3) - (point+ni))
            if length < len(str(board[i][k])):
                length = len(str(board[i][k]))

for x in range(a):
    for y in range(b):
        print('{}{}'.format((' '*(length-len(str(board[x][y])))), board[x][y]), end=" ")
    print()