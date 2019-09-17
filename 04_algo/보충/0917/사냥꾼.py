import sys
sys.stdin = open('사냥꾼.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    check = 1

    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                x, y = j, i
                while check:
                    if x < 0 or x >= N or y < 0 or y >= N or data[y][x] == 3:
                        x, y = j, i
                        break
                    elif data[y][x] == 2:
                        cnt += 1
                    x += 1

                while check:
                    if x < 0 or x >= N or y < 0 or y >= N or data[y][x] == 3:
                        x, y = j, i
                        break
                    elif data[y][x] == 2:
                        cnt += 1
                    x -= 1
                while check:
                    if x < 0 or x >= N or y < 0 or y >= N or data[y][x] == 3:
                        x, y = j, i
                        break
                    elif data[y][x] == 2:
                        cnt += 1
                    y += 1
                while check:
                    if x < 0 or x >= N or y < 0 or y >= N or data[y][x] == 3:
                        x, y = j, i
                        break
                    elif data[y][x] == 2:
                        cnt += 1
                    y -= 1
                while check:
                    if x < 0 or x >= N or y < 0 or y >= N or data[y][x] == 3:
                        x, y = j, i
                        break
                    elif data[y][x] == 2:
                        cnt += 1
                    x += 1
                    y += 1

                while check:
                    if x < 0 or x >= N or y < 0 or y >= N or data[y][x] == 3:
                        x, y = j, i
                        break
                    elif data[y][x] == 2:
                        cnt += 1
                    x += 1
                    y -= 1

                while check:
                    if x < 0 or x >= N or y < 0 or y >= N or data[y][x] == 3:
                        x, y = j, i
                        break
                    elif data[y][x] == 2:
                        cnt += 1
                    x -= 1
                    y += 1

                while check:
                    if x < 0 or x >= N or y < 0 or y >= N or data[y][x] == 3:
                        x, y = j, i
                        break
                    elif data[y][x] == 2:
                        cnt += 1
                    x -= 1
                    y -= 1







    print('#{} {}'.format(tc, cnt))