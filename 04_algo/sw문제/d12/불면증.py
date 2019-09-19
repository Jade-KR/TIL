import sys
sys.stdin = open('불면증.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tmp = set()
    cnt = 1

    while len(tmp) != 10:
        a = N*cnt
        for i in str(a):
            tmp.add(int(i))
        cnt += 1
    cnt -= 1
    print('#{} {}'.format(tc, cnt*N))
