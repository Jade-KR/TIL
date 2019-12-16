import sys
sys.stdin = open("새로운게임.txt")
import collections

def bfs(x, y, fd, ld, out):
    global cnt, ans, change, K

    while len(q):
        cnt += 1
        if cnt == K:
            cnt = 0
            ans += 1
            K = K - change
            change = 0
        if out >= 4:
            return
        if ans >= 1000:
            ans = -1
            return
        nx, ny, nfd = q.popleft()
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
                    change += 1
                    out += 1
                else:
                    visited[x][y] = 0
                    visited[nx][ny] = nld
                    q.append((nx, ny, nfd))

            # 빨간 칸 일 때
            elif board[nx][ny] == 1:
                if visited[nx][ny]:
                    visited[x][y] = 0
                    visited[nx][ny] = nfd
                    change += 1
                    out += 1
                else:
                    visited[x][y] = 0
                    visited[nx][ny] = nfd
                    q.append((nx, ny, nld))

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

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                if nfd == 1:
                    ny -= 1
                elif nfd == 2:
                    ny += 1
                elif nfd == 3:
                    nx -= 1
                elif nfd == 4:
                    nx += 1
                q.append((0, 0, 0))

            # 흰 칸 일 때
            elif board[nx][ny] == 0:
                if visited[nx][ny]:
                    visited[x][y] = 0
                    visited[nx][ny] = nld
                    out += 1
                    change += 1
                else:
                    visited[x][y] = 0
                    visited[nx][ny] = nld
                    q.append((nx, ny, nfd))

            # 빨간 칸 일 때
            elif board[nx][ny] == 1:
                if visited[nx][ny]:
                    visited[x][y] = 0
                    visited[nx][ny] = nfd
                    out += 1
                    change += 1
                else:
                    visited[x][y] = 0
                    visited[nx][ny] = nfd
                    q.append((nx, ny, nld))

        # 흰 칸 일 때
        elif board[nx][ny] == 0:
            if visited[nx][ny]:
                visited[x][y] = 0
                visited[nx][ny] = nld
                out += 1
                change += 1
            else:
                visited[x][y] = 0
                visited[nx][ny] = nld
                q.append((nx, ny, nfd))

        # 빨간 칸 일 때
        elif board[nx][ny] == 1:
            if visited[nx][ny]:
                visited[x][y] = 0
                visited[nx][ny] = nfd
                out += 1
                change += 1
            else:
                visited[x][y] = 0
                visited[nx][ny] = nfd
                q.append((nx, ny, nld))


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
pieces = [list(map(int, input().split())) for _ in range(K)]
stack = 1
cnt = 0
ans = 0
change = 0
visited = [[0]*N for _ in range(N)]
q = collections.deque()

for i in range(K):
    visited[pieces[i][0]-1][pieces[i][1]-1] = pieces[i][2]
    q.append((pieces[i][0]-1, pieces[i][1]-1, pieces[i][2]))

bfs(0, 0, 0, 0, 1)

print(ans)