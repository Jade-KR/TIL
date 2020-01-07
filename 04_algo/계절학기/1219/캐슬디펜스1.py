import sys
sys.stdin = open('캐슬디펜스.txt')


def comb(dep=0):
    global game, check, kill, target, ans
    if len(arr) == 3:
        check = 0
        game = [[0] * M for _ in range(N + 1)]
        for i in range(N):
            for j in range(M):
                if data[i][j] == 1:
                    game[i][j] = 1
        for a in range(3):
            game[N][arr[a]] = 3
        while check == 0:
            target = []
            for q in range(N + 1):
                for w in range(M):
                    if game[q][w] == 3:
                        d = 9876543
                        x, y = -1, -1
                        for e in range(N):
                            for r in range(M):
                                if game[e][r] == 1:
                                    tmp = abs(q - e) + abs(w - r)
                                    if tmp <= D:
                                        if d > tmp:
                                            x, y = e, r
                                            d = tmp
                                        if d == tmp:
                                            if y > r:
                                                x, y = e, r
                                                d = tmp
                        if x >= 0 and y >= 0:
                            target.append([x, y])

            # 타겟 죽이기
            for nx, ny in target:
                if game[nx][ny] == 1:
                    game[nx][ny] = 0
                    kill += 1

            # 타겟 없으면 나오고 있으면 한칸씩 내려오기
            check = 1
            B = []
            for i in range(N + 1):
                for j in range(M):
                    if game[i][j] == 1:
                        if i < N:
                            B.append([i, j])

            game = [[0] * M for _ in range(N + 1)]
            for nx, ny in B:
                if nx < N:
                    game[nx + 1][ny] = 1

            for p in range(M):
                game[N][p] = 0

            for i in range(N + 1):
                for j in range(M):
                    if game[i][j] == 1:
                        check = 0
            for a in range(3):
                game[N][arr[a]] = 3

        if ans < kill:
            ans = kill
        kill = 0
        return
    if dep == len(A):
        return
    for k in range(dep, len(A)):
        arr.append(A[k])
        comb(k + 1)
        arr.pop()


N, M, D = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)] + [[0] * M]
game = [[0] * M for _ in range(N + 1)]
for i in range(N):
    for j in range(M):
        if data[i][j] == 1:
            game[i][j] = 1

A = [i for i in range(M)]
arr = []
check = 0
kill = 0
ans = 0
comb()

print(ans)