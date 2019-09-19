import sys
sys.stdin = open('극장좌석.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    data.sort()
    cnt = 0

    for i in data:
        cnt += i*2

    vl = [0]*cnt

    for i in range(data[-1]*2+1):
        vl[i] = 1

    for i in range(len(data)-2, -1, -1):
        flag = 0
        ck = 0
        while flag <= data[i]:
            if vl[ck] == 0:
                vl[ck] = 1
                flag += 1
            ck += 1

    print('#{} {}'.format(tc, vl.count(1)))


