import sys
sys.stdin = open("새로운게임.txt")
import collections
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
pieces = [list(map(int, input().split())) for _ in range(K)]
check = [0 for _ in range(K)]
stack = 1
cnt = 0
ans = 0
finish = 0
change = 0
out = 1
visited = [[0]*N for _ in range(N)]
q = collections.deque()
for i in range(K):
    visited[pieces[i][0]-1][pieces[i][1]-1] = pieces[i][2]
    q.append((pieces[i][0]-1, pieces[i][1]-1, pieces[i][2]))

# 번호 체크하고 말 개수 체크
while finish == 0:
    if ans >= 1000:
        ans = -1
        break

    for z in range(K):
        if check[z] == 1:
            continue
        else:
            nx, ny, nfd = pieces[z][0]-1, pieces[z][1]-1, pieces[z][2]
            x, y = nx, ny
            nld = visited[nx][ny]
            if nfd == 1:
                ny += 1
            elif nfd == 2:
                ny -= 1
            elif nfd == 3:
                nx -= 1
            elif nfd == 4:
                nx += 1

            # 판 밖으로 나갈 때
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                if nfd % 2 == 1:
                    nfd += 1
                else:
                    nfd -= 1
                if nfd == 1:
                    ny += 2
                elif nfd == 2:
                    ny -= 2
                elif nfd == 3:
                    nx -= 2
                elif nfd == 4:
                    nx += 2

                # 파란 칸 일 때
                if board[nx][ny] == 2:
                    if nfd == 1:
                        ny -= 1
                    elif nfd == 2:
                        ny += 1
                    elif nfd == 3:
                        nx -= 1
                    elif nfd == 4:
                        nx += 1

                # 흰 칸 일 때
                elif board[nx][ny] == 0:
                    if visited[nx][ny]:
                        visited[x][y] = 0
                        visited[nx][ny] = nld
                    else:
                        visited[x][y] = 0
                        visited[nx][ny] = nld
                # 빨간 칸 일 때
                elif board[nx][ny] == 1:
                    if visited[nx][ny]:
                        visited[x][y] = 0
                        visited[nx][ny] = nfd
                    else:
                        visited[x][y] = 0
                        visited[nx][ny] = nfd
                        nfd = nld

            # 파란 칸 일 때
            elif board[nx][ny] == 2:
                if nfd % 2 == 1:
                    nfd += 1
                else:
                    nfd -= 1
                if nfd == 1:
                    ny += 2
                elif nfd == 2:
                    ny -= 2
                elif nfd == 3:
                    nx -= 2
                elif nfd == 4:
                    nx += 2

                # 벽 만났을때
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    if nfd == 1:
                        ny -= 1
                    elif nfd == 2:
                        ny += 1
                    elif nfd == 3:
                        nx -= 1
                    elif nfd == 4:
                        nx += 1

                # 흰 칸 일 때
                elif board[nx][ny] == 0:
                    if visited[nx][ny]:
                        visited[x][y] = 0
                        visited[nx][ny] = nld
                    else:
                        visited[x][y] = 0
                        visited[nx][ny] = nld
                # 빨간 칸 일 때
                elif board[nx][ny] == 1:
                    if visited[nx][ny]:
                        visited[x][y] = 0
                        visited[nx][ny] = nfd
                    else:
                        visited[x][y] = 0
                        visited[nx][ny] = nfd
                        nfd = nld
            # 흰 칸 일 때
            elif board[nx][ny] == 0:
                if visited[nx][ny]:
                    visited[x][y] = 0
                    visited[nx][ny] = nld
                else:
                    visited[x][y] = 0
                    visited[nx][ny] = nld
            # 빨간 칸 일 때
            elif board[nx][ny] == 1:
                if visited[nx][ny]:
                    visited[x][y] = 0
                    visited[nx][ny] = nfd
                else:
                    visited[x][y] = 0
                    visited[nx][ny] = nfd
                    nfd = nld

            pieces[z][0], pieces[z][1], pieces[z][2] = nx, ny, nfd
print(ans)