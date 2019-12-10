import sys
sys.stdin = open('원판돌리기.txt')


N, M, T = map(int, input().split())
circle = [list(map(int, input().split())) for _ in range(N)]
info = [list(map(int, input().split())) for _ in range(T)]
ans = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(T):
    visited = [[0] * M for _ in range(N)]
    if info[i][1] == 0:
        # 원판 돌리기 (시계방향)
        for k in range(info[i][2]):
            num = info[i][0]
            while num <= N:
                t = circle[num-1].pop()
                circle[num-1].insert(0, t)
                num = num + num
        # 인접한 것들 중 같은 값 체크
        for a in range(N):
            for b in range(M):
                if circle[a][b] != -1000:
                    for k in range(4):
                        na = a + dx[k]
                        nb = b + dy[k]
                        if na < 0 or na >= N or nb >= M: continue
                        if circle[a][b] == circle[na][nb]:
                            visited[a][b] = 1
                            visited[na][nb] = 1

        check = 0
        # 인접한 값이 같은 것을 지울때
        for i in range(N):
            for j in range(M):
                if visited[i][j]:
                    circle[i][j] = -1000
                    check = 1
        # 인접할 값을 지울 수 없을때
        if check == 0:
            sum_c = 0
            cnt = 0
            c = 0
            for i in range(N):
                for j in range(M):
                    if circle[i][j] == -1000:
                        cnt += 1
                    else:
                        sum_c += circle[i][j]
            #평균 구하기
            c = M*N - cnt
            if c != 0:
                avg = sum_c / c

                #평균 보다 크거나 작은 값 +- 1
                for h in range(N):
                    for k in range(M):
                        if circle[h][k] > avg and circle[h][k] != -1000:
                            circle[h][k] -= 1
                        elif circle[h][k] < avg and circle[h][k] != -1000:
                            circle[h][k] += 1
            else:
                break

    elif info[i][1] == 1:
        # 원판 돌리기 (반시계방향)
        for k in range(info[i][2]):
            num = info[i][0]
            while num <= N:
                t = circle[num - 1].pop(0)
                circle[num - 1].append(t)
                num = num + num
        # 인접한 것들 중 같은 값 체크
        for a in range(N):
            for b in range(M):
                if circle[a][b] != -1000:
                    for k in range(4):
                        na = a + dx[k]
                        nb = b + dy[k]
                        if na < 0 or na >= N or nb >= M: continue
                        if circle[a][b] == circle[na][nb]:
                            visited[a][b] = 1
                            visited[na][nb] = 1

        check = 0
        # 인접한 값이 같은 것을 지울 때
        for i in range(N):
            for j in range(M):
                if visited[i][j]:
                    circle[i][j] = -1000
                    check = 1

        # 인접한 값을 지울 것이 없을 때
        if check == 0:
            sum_c = 0
            cnt = 0
            c = 0
            for i in range(N):
                for j in range(M):
                    if circle[i][j] == -1000:
                        cnt += 1
                    else:
                        sum_c += circle[i][j]
            # 평균 구하기
            c = M*N - cnt
            if c != 0:
                avg = sum_c / c

                # 평균 보다 크거나 작은 값 +- 1
                for h in range(N):
                    for k in range(M):
                        if circle[h][k] > avg and circle[h][k] != -1000:
                            circle[h][k] -= 1
                        elif circle[h][k] < avg and circle[h][k] != -1000:
                            circle[h][k] += 1
            else:
                break

for i in range(N):
    for j in range(M):
        if circle[i][j] > 0:
            ans += circle[i][j]

print(ans)