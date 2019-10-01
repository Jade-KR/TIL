import sys
sys.stdin = open('암호생성기.txt')

T = 10
for tc in range(1, T+1):
    n = int(input())
    data = list(map(int, input().split()))
    check = 0
    cnt = 0
    while check != 1:
        t = data.pop(0)
        if t-(cnt%5+1) <= 0:
            check = 1
            data.append(0)
            break
        data.append(t-(cnt%5+1))
        cnt += 1

    print('#{} '.format(tc), end='')
    for i in data:
        print(i, end=' ')
    print()