import sys
sys.stdin = open('이진수.txt')

T = int(input())
for tc in range(1, T+1):
    N, data = map(str, input().split())
    tmp = ''

    for i in data:
        if '0' <= i <= '9':
            if len(bin(int(i))) == 3:
                tmp += '000' + bin(int(i))[2::]
            elif len(bin(int(i))) == 4:
                tmp += '00' + bin(int(i))[2::]
            elif len(bin(int(i))) == 5:
                tmp += '0' + bin(int(i))[2::]
            else:
                tmp += bin(int(i))[2::]
        else:
            tmp += bin(ord(i) - ord('A') + 10)[2:]


    print('#{} {}'.format(tc, tmp))