import collections
import sys
sys.stdin = open('특이한자석.txt')

def work(n, d):
    global magnet
    if d == 1:
        t = magnet[n].pop()
        magnet[n].insert(0, t)
        if magnet[n+1][6] != magnet[n][3]:
            t = magnet[n+1].pop(0)
            magnet[n+1].append(t)
            if magnet[n+2][6] != magnet[n+1][1]:
                t = magnet[n+2].pop()
                magnet[n+2].insert(0, t)
                if magnet[n + 3][6] != magnet[n + 2][3]:
                    t = magnet[n + 3].pop(0)
                    magnet[n + 3].append(t)
    elif d == -1:
        t = magnet[n].pop(0)
        magnet[n].append(t)
        if magnet[n+1][6] != magnet[n][1]:
            t = magnet[n+1].pop()
            magnet[n+1].insert(0, t)
            if magnet[n+2][6] != magnet[n+1][3]:
                t = magnet[n+2].pop(0)
                magnet[n+2].append(t)
                if magnet[n + 3][6] != magnet[n+2][1]:
                    t = magnet[n + 3].pop()
                    magnet[n + 3].insert(0, t)
# 앞, 뒤 고려해야함.
def work2(n, d):
    global magnet
    check1 = 0
    check4 = 0
    if d == 1:
        t = magnet[n].pop()
        magnet[n].insert(0, t)

        if magnet[n - 1][2] != magnet[n][7]:
            t = magnet[n - 1].pop(0)
            magnet[n - 1].append(t)
            if n == 2:
                check1 = 1

        if magnet[n + 1][6] != magnet[n][3]:
            t = magnet[n + 1].pop(0)
            magnet[n + 1].append(t)
            if n == 1:
                check4 = 1

        if n == 1:
            if check4 == 1:
                if magnet[3][6] != magnet[2][1]:
                    t = magnet[3].pop()
                    magnet[3].insert(0, t)

        if n == 2:
            if check1 == 1:
                if magnet[0][2] != magnet[1][5]:
                    t = magnet[0].pop()
                    magnet[0].insert(0, t)

    elif d == -1:
        t = magnet[n].pop(0)
        magnet[n].append(t)

        if magnet[n - 1][2] != magnet[n][5]:
            t = magnet[n - 1].pop()
            magnet[n - 1].insert(0, t)
            if n == 2:
                check1 = 1

        if magnet[n + 1][6] != magnet[n][1]:
            t = magnet[n + 1].pop()
            magnet[n + 1].insert(0, t)
            if n == 1:
                check4 = 1

        if n == 1:
            if check4 == 1:
                if magnet[3][6] != magnet[2][3]:
                    t = magnet[3].pop(0)
                    magnet[3].append(t)

        if n == 2:
            if check1 == 1:
                if magnet[0][2] != magnet[1][7]:
                    t = magnet[0].pop(0)
                    magnet[0].append(t)

def work3(n, d):
    global magnet
    if d == 1:
        t = magnet[n].pop()
        magnet[n].insert(0, t)
        if magnet[n-1][2] != magnet[n][7]:
            t = magnet[n-1].pop(0)
            magnet[n-1].append(t)
            if magnet[n-2][2] != magnet[n-1][5]:
                t = magnet[n-2].pop()
                magnet[n-2].insert(0, t)
                if magnet[n-3][2] != magnet[n-2][7]:
                    t = magnet[n-3].pop(0)
                    magnet[n-3].append(t)

    elif d == -1:
        t = magnet[n].pop(0)
        magnet[n].append(t)
        if magnet[n-1][2] != magnet[n][5]:
            t = magnet[n-1].pop()
            magnet[n-1].insert(0, t)
            if magnet[n-2][2] != magnet[n-1][7]:
                t = magnet[n-2].pop(0)
                magnet[n-2].append(t)
                if magnet[n-3][2] != magnet[n-2][5]:
                    t = magnet[n-3].pop()
                    magnet[n-3].insert(0, t)

def rotation(n, d):
    global magnet
    if n == 0:
        work(n, d)

    if n == 1:
        work2(n, d)

    if n == 2:
        work2(n, d)

    if n == 3:
        work3(n, d)


T = int(input())
for tc in range(1, T+1):
    K = int(input())
    magnet = [list(map(int, input().split())) for _ in range(4)]
    turn = [list(map(int, input().split())) for _ in range(K)]
    cnt = 0
    # magnet 에서 0 = N , 1 = S 극, 인덱스 번호 2번이 다음 자석과 연결, 6번이 이전의 자석과 연결

    for i in range(K):
        rotation(turn[i][0]-1, turn[i][1])


    for c in range(4):
        if magnet[c][0] == 1:
            if c == 0:
                cnt += 1
            elif c == 1:
                cnt += 2
            elif c == 2:
                cnt += 4
            elif c == 3:
                cnt += 8

    print('#{} {}'.format(tc, cnt))
    # turn에서 1 = 시계방향, -1 = 반시계방향

















