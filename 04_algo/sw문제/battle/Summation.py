import sys
sys.stdin = open('Summation.txt')

T = int(input())
for tc in range(1, T+1):
    data = list(map(str, input().split()))
    min_d = 987654321
    max_d = 0

    for i in data:
        tmp = 0
        for j in i:
            tmp += int(j)
        if min_d > tmp:
            min_d = tmp
        if max_d < tmp:
            max_d = tmp

    print('#{} {} {}'.format(tc, max_d, min_d))
