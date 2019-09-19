import sys
sys.stdin = open('최빈수.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))
    min_s = 0
    num = 0

    for i in range(101):
        if min_s <= score.count(i):
            min_s = score.count(i)
            num = i


    print('#{} {}'.format(tc, num))