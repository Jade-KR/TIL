import sys
sys.stdin = open("유턴싫어.txt")

R, C = map(int, input().split())
data = [list(map(str, input())) for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0

for i in range(R):
    if ans == 1:
        break
    for j in range(C):
        if ans == 1:
            break
        if data[i][j] == '.':
            cnt = 0
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < R and 0 <= nj < C:
                    if data[ni][nj] == '.':
                        cnt += 1
            if cnt < 2:
                ans = 1

print(ans)