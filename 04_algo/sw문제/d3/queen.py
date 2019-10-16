import sys
sys.stdin = open('queen.txt')

def dfs(x, y, cy):
    global ans
    c = 0
    if x == N:
        ans += 1
        return

    for y in range(N):
        if y == cy+1 and y == cy-1 and x > 0:
            continue
        if visited[y] == 1:
            continue
        c = 0
        if x != 0:
            for d in range(N):
                if 0 <= x-d and y+d < N:
                    if nxn[x-d][y+d] == 1:
                        c = 1
                        break
                if 0 <= x - d and 0 <= y - d:
                    if nxn[x-d][y-d] == 1:
                        c = 1
                        break
        if c == 1:
            continue
        visited[y] = 1
        nxn[x][y] = 1
        dfs(x+1, y, 0)
        visited[y] = 0
        nxn[x][y] = 0

T = int(input())
for test in range(T):
    N = int(input())
    nxn = [[0 for _ in range(N)]for _ in range(N)]
    visited = [0 for _ in range(N)]
    ans = 0

    dfs(0, 0, 0)

    print("#%d %d" % (test+1, ans))