import sys
sys.stdin = open('거스름돈.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    m1 = 0
    m2 = 0
    m3 = 0
    m4 = 0
    m5 = 0
    m6 = 0
    m7 = 0
    m8 = 0

    if N // 50000:
        m1 = N // 50000
        N = N - 50000 * m1
    if N // 10000:
        m2 = N // 10000
        N = N - 10000 * m2
    if N // 5000:
        m3 = N // 5000
        N = N - 5000 * m3
    if N // 1000:
        m4 = N // 1000
        N = N - 1000 * m4
    if N // 500:
        m5 = N // 500
        N = N - 500 * m5
    if N // 100:
        m6 = N // 100
        N = N - 100 * m6
    if N // 50:
        m7 = N // 50
        N = N - 50 * m7
    if N // 10:
        m8 = N // 10
        N = N - 10 * m8

    print('#{}'.format(tc))
    print('{} {} {} {} {} {} {} {}'.format(m1, m2, m3, m4, m5, m6, m7, m8))