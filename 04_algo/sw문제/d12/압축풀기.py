import sys
sys.stdin = open('압축풀기.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(input().split()) for _ in range(N)]
    tmp = ''
    print('#{}'.format(tc))
    for i in range(N):
        tmp += data[i][0] * int(data[i][1])

    for j in range(0, len(tmp)):
        if j % 10 == 0 and j != 0:
            print()
        print(tmp[j], end='')
    print()