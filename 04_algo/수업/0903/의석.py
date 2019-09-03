import sys
sys.stdin = open('의석.txt')

T = int(input())
for tc in range(1, T+1):
    data = [input() for _ in range(5)]
    max_d = 0 # 문자 최대 길이
    check = ''
    for i in range(5):
        if max_d < len(data[i]):
            max_d = len(data[i])

    for i in range(max_d):
        for j in range(5):
            if i >= len(data[j]):
                continue
            else:
                check += data[j][i]
    print('#{} {}'.format(tc, check))