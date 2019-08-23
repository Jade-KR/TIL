import sys
sys.stdin = open("숫자 카드.txt")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    a = list(input())
    tmp = []
    for i in a:
        tmp.append(a.count(i))

    for j in range(len(tmp) - 1, 0, -1):
        for k in range(0, j):
            if tmp[k] > tmp[k + 1]:
                tmp[k], tmp[k + 1] = tmp[k + 1], tmp[k]
    pro = tmp[-1]

    if pro == 1:
        for o in range(len(a) - 1, 0, -1):
            for p in range(0, o):
                if a[p] > a[p + 1]:
                    a[p], a[p + 1] = a[p + 1], a[p]
        result = a[-1]
    else:
        result = a[(tmp.index(pro))]

    print('#{} {} {}'.format(test_case, result, pro))

