def power(a, b, x):
    global flag, ans
    if flag == 1:
        return
    if b <= 1:
        flag = 1
        ans = x
    x = x*a
    power(a, b-1, x)

import sys
sys.stdin = open('거듭제곱.txt', 'rt', encoding='utf-8')

T = 10
for tc in range(1, T+1):
    t = int(input())
    num, c = map(int, input().split())
    flag = 0
    ans = 0

    power(num, c, num)
    print('#{} {}'.format(tc, ans))