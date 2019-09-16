import sys
sys.stdin = open('2진암호코드.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    cmp = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    key = 0
    for i in data:
        if int(i) != 0:
            pw = i

    cnt = len(pw)

    for i in range(len(pw)-1, -1, -1):
        if pw[i] == '1':
            break
        cnt -= 1
    key = cnt-56

    code = ''

    for i in range(key, len(pw), 7):
        if pw[i: i + 7] in cmp:
            code += str(cmp.index(pw[i: i+7]))

    even = 0
    odd = 0
    verify = 0
    result = 0
    for j in range(len(code)):
        if j % 2 == 1:
            even += int(code[j])
        elif j == 7:
            verify += int(code[j])
        else:
            odd += int(code[j])

    if (odd*3 + even + verify) % 10 == 0:
        result = even+odd+verify
    else:
        result = 0

    print('#{} {}'.format(tc, result))