import sys
sys.stdin = open('1.txt')

T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    max_d = data[0]
    min_d = data[0]
    for i in data:
        if max_d < i:
            max_d = i
        if min_d > i:
            min_d = i

    sum_d = 0

    for i in data:
        sum_d += i

    result = (sum_d - (max_d + min_d)) / (len(data)-2)

    print('#{} {}'.format(tc, round(result)))
