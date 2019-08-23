import sys
sys.stdin = open("구간합.txt")

T = int(input())
for test_case in range(1, T + 1):
    N, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    tmp = []
    for i in range(N-m+1):
        sum_num = 0
        for j in range(i, i+m):
            sum_num += a[j]
        tmp.append(sum_num)

    min_num = tmp[0]
    max_num = tmp[0]

    for k in tmp:
        if k < min_num:
            min_num = k
        if k > max_num:
            max_num = k



    result = max_num - min_num
    print('#{} {}'.format(test_case, result))