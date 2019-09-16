import sys
sys.stdin = open('두개의숫자열.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max_ab = 0


    if len(b) > len(a):
        for i in range(len(b) - len(a) + 1):
            tmp = 0
            for j in range(len(a)):
                tmp += a[j] * b[j+i]
            if max_ab < tmp:
                max_ab = tmp

    elif len(a) > len(b):
        for i in range(len(a) - len(b) + 1):
            tmp = 0
            for j in range(len(b)):
                tmp += b[j] * a[j+i]
            if max_ab < tmp:
                max_ab = tmp

    else:
        for i in range(len(a)):
            tmp = 0
            for j in range(len(a)):
                tmp += b[j] * a[j]
            if max_ab < tmp:
                max_ab = tmp

    print('#{} {}'.format(tc, max_ab))
