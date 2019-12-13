import sys
sys.stdin= open('주사위윷놀이.txt')
dice = list(map(int, input().split()))
board = [[i*2 for i in range(0, 21)], [0]*21, [0]*21, [0]*21, [0]*21, [0]*21, [0]*21, [0]*21]
board[1][5], board[1][10], board[1][15] = 13, 22, 28
board[2][5], board[2][10], board[2][15] = 16, 24, 27
board[3][5], board[3][15] = 19, 26
board[4][5], board[3][10], board[4][15] = 25, 25, 25
board[5][5], board[4][10], board[5][15] = 30, 30, 30
board[6][5], board[5][10], board[6][15] = 35, 35, 35
board[7][5], board[6][10], board[7][15] = 40, 40, 40

visited = [[0]*21 for _ in range(7)]


