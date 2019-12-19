import sys
sys.stdin = open("파이프옮기기.txt")

def dfs(x, y, d):
    global ans
    if x == N-1 and y == N-1:
        ans += 1
        return

    if d == 0:
        if 0 <= x + 1 < N and 0 <= y+1 < N:
            if data[x][y+1] == 0 and data[x+1][y] == 0 and data[x+1][y+1] == 0:
                dfs(x+1, y+1, 1)

        if 0 <= y+1 < N:
            if data[x][y+1] == 0:
                dfs(x, y+1, 0)

    elif d == 1:
        if 0 <= x + 1 < N and 0 <= y+1 < N:
            if data[x][y+1] == 0 and data[x+1][y] == 0 and data[x+1][y+1] == 0:
                dfs(x+1, y+1, 1)

        if 0 <= y+1 < N:
            if data[x][y+1] == 0:
                dfs(x, y+1, 0)

        if 0 <= x+1 < N:
            if data[x+1][y] == 0:
                dfs(x+1, y, 2)

    elif d == 2:
        if 0 <= y+1 < N and 0 <= x+1 < N:
            if data[x][y+1] == 0 and data[x+1][y] == 0 and data[x+1][y+1] == 0:
                dfs(x+1, y+1, 1)

        if 0 <= x+1 < N:
            if data[x+1][y] == 0:
                dfs(x+1, y, 2)




N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
ans = 0

dfs(0, 1, 0)
print(ans)