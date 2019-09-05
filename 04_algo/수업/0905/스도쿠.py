import sys
sys.stdin = open('스도쿠.txt')

T = int(input())
for tc in range(1, T+1):
    data = [list(map(int, input().split())) for _ in range(9)]
    sum_a = 0
    check = 0
    for i in range(1, 10):
        sum_a += i

    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            sum_b = 0
            for k in range(3):
                for l in range(3):
                    sum_b += data[k+i][l+j]
            if sum_b != sum_a:
                check += 1


    for i in range(9):
        sum_b = 0
        for j in range(9):
            sum_b += data[i][j]
        if sum_b != sum_a:
            check += 1

    for i in range(9):
        sum_b = 0
        for j in range(9):
            sum_b += data[j][i]
        if sum_b != sum_a:
            check += 1

    if check == 0:
        result = 1
    else:
        result = 0

    print('#{} {}'.format(tc, result))