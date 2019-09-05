import sys
sys.stdin = open('스도쿠.txt')

T = int(input())
for tc in range(1, T+1):
    data = [list(map(int, input().split())) for _ in range(9)]
    check = set()
    result = 1

    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            for k in range(3):
                for l in range(3):
                    check.add(data[k+i][l+j])
            if check != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                result = 0
            check = set()


    for i in range(9):
        for j in range(9):
            check.add(data[i][j])
        if check != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            result = 0
        check = set()

    for i in range(9):
        for j in range(9):
            check.add(data[j][i])
        if check != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            result = 0
        check = set()

    print('#{} {}'.format(tc, result))