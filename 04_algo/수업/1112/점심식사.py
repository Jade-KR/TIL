import sys
sys.stdin = open('점심식사.txt')

def powerset(n, k):     # n: 원소의 갯수, k: 현재 depth
    global t, tm
    if n == k: #  Basis part
        st1 = []
        st2 = []
        t1 = []
        t2 = []
        tmp = []
        for i in range(n):
            if vl[i] == 1:
                st1.append(d1[i])
            else:
                st2.append(d2[i])

        # 먼저 도착한 애들 시간지나면 사라져야함.
        st1 = sorted(st1)
        st2 = sorted(st2)
        # 3명 계단에 있으면 기다려야함.
        if len(st1) > 3:
            while st1:

                tm += 1

        tm = 0

        print(st1)
        print(st2)
        print()

        if st1:
            max_t = max(st1)
            if st2:
                if max_t < max(st2):
                    max_t = max(st2)
                if t > max_t:
                    t = max_t
    else:
        vl[k] = 1
        powerset(n, k + 1) # 다음 요소 포함 여부 결정
        vl[k] = 0
        powerset(n, k + 1) # 다음 요소 포함 여부 결정


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    stair = []
    t = 987654321
    tm = 0
    d1 = []
    d2 = []
    for i in range(N):
        for j in range(N):
            if data[i][j] > 1:
                stair.append([i, j, data[i][j]])

    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                d1.append(abs(i-stair[0][0]) + abs(j - stair[0][1]) + 1)
                d2.append(abs(i-stair[1][0]) + abs(j - stair[1][1]) + 1)

    vl = [0] * len(d1)
    powerset(len(vl), 0)