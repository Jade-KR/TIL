import sys
sys.stdin = open('이진수2.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    tmp = ''

    while len(tmp) <= 13:
        if N*2 == 1:
            tmp += '1'
            break
        elif N*2 > 1:
            tmp += '1'
            N = N*2 - 1
        elif N*2 < 1:
            tmp += '0'
            N = N*2
    if len(tmp) >= 13:
        tmp = 'overflow'
    print(tmp)