import sys
sys.stdin = open("게리맨더링2.txt")


def checkLine():
    chk = 0
    e1, e2 = 1, 1
    while chk == 0:
        flag = 0
        if 1 <= e1 < y:
            d1.append(e1)
        else:
            flag += 1
        if 1 <= e2 <= N - y:
            d2.append(e2)
            flag += 1
        e1 += 1
        e2 += 1
        if flag == 2:
            chk = 1


def makeBorder(nx, ny, t1, t2):
    e1, e2 = 0, 0
    chk = 0
    # 1, 4 구역 경계선
    while chk == 0:
        if e1 == t1:
            chk = 1
        board[nx+e1][ny-e1] = 5
        board[nx+t2+e1][ny+t2-e1] = 5
        if e1 < t1:
            e1 += 1

    # 2, 3 구역 경계선
    chk = 0
    while chk == 0:
        if e2 == t2:
            chk = 1
        board[nx+e2][ny+e2] = 5
        board[nx+e2+t1][ny+e2-t1] = 5
        if e2 < t2:
            e2 += 1

def checkPopulation(nx, ny, t1, t2):
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0 and 0 <= r < nx+t1 and 0 <= c <= ny:
                board[r][c] = 1
                eachPopulation[1] += population[r][c]

            elif board[r][c] == 0 and 0 <= r <= nx+t2 and ny < c < N:
                board[r][c] = 2
                eachPopulation[2] += population[r][c]

            elif board[r][c] == 0 and nx+t1 <= r < N and 0 <= c < ny-t1+t2:
                board[r][c] = 3
                eachPopulation[3] += population[r][c]

            elif board[r][c] == 0 and nx+t2 < r < N and ny-t1+t2 <= c < N:
                board[r][c] = 4
                eachPopulation[4] += population[r][c]
            else:
                board[r][c] = 5
                eachPopulation[5] += population[r][c]


N = int(input())
population = [list(map(int, input().split())) for _ in range(N)]
eachPopulation = [0, 0, 0, 0, 0, 0]
ans = 987654321
# d1, d2 중복 조합 사용

# 1 <= d1, d2

# d2 <= N - y

# d1 < y

# d1 + d2 <= N - x

# 기준 점을 잡고 d1, d2 값을 정한다. (중복 조합으로)
# 경계선을 잇고 각 구역의 인구수를 구역별로 나눠 계산한다.
# 가장 많은 구역과 적은 구역의 차의 최솟값을 구한다.

for i in range(N):
    for j in range(N):
        x, y = i + 1, j + 1
        d1 = []
        d2 = []
        checkLine()

        for a in d1:
            for b in d2:
                if a + b <= N - x:
                    board = [[0] * N for _ in range(N)]
                    makeBorder(x-1, y-1, a, b)
                    checkPopulation(x-1, y-1, a, b)
                    result = max(eachPopulation) - min(eachPopulation)
                    if ans > result:
                        ans = result

print(ans)