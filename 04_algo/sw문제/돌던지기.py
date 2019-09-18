import sys
sys.stdin = open('돌던지기.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = list(map(int, input().split()))
    tmp = []

    for i in d:
        tmp.append(abs(i))

    min_t = min(tmp)
    num = tmp.count(min(tmp))
    print('#{} {} {}'.format(tc, min_t, num))