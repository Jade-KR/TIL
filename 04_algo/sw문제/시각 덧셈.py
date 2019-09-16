import sys
sys.stdin = open('시각 덧셈.txt')

T = int(input())
for tc in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())

    h3 = h1+h2

    if m1+m2 >= 60:
        h3 += 1
        m3 = m1+m2-60
    else:
        m3 = m1+m2

    if h3 > 12:
        h3 -= 12

    print('#{} {} {}'.format(tc, h3, m3))