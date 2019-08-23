import sys
sys.stdin = open("전기버스.txt")

T = int(input())

for test_case in range(1, T+1):
    move, end, cnt = map(int, input().split())
    charger = list(map(int, input().split()))

    all = [0]*(end-1)
    for i in range(end):
        if i+1 in charger:
            all[i]=i+1
    p = 0
    check = 1
    charge = 0
    while check:
        if p + move >= end:
            check = 0
            break

        for j in range(move+1):
            if j == move:
                check = 0
                charge = 0
                break
            if all[p+move-1-j]:
                p += move-j
                charge += 1
                break


    print('#{} {}'.format(test_case, charge))



