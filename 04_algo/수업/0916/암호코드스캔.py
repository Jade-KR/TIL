import sys
sys.stdin = open('암호코드스캔.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    cmp = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    for i in cmp:
        i[0]*N//100
        i[1] * N // 100
        i[2] * N // 100
        i[3] * N // 100
        i[4] * N // 100
        i[5] * N // 100
        i[6] * N // 100
        i[7] * N // 100

    pw = []
    for i in data:
        try:
            if int(i) != 0:
                if i in pw:
                    continue
                else:
                    pw.append(i)

        except:
            if i in pw:
                continue
            else:
                pw.append(i)

    tmp = ''
    pwd = []
    for k in range(len(pw)):
        tmp = ''
        for i in pw[k]:
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
        pwd.append(tmp)
    cnt = len(tmp)
    for i in range(len(tmp)-1, -1, -1):
        if tmp[i] == '1':
            break
        cnt -= 1
    key = cnt-56

    code = ''

    for i in range(key, len(tmp), 7):
        if tmp[i: i + 7] in cmp:
            code += str(cmp.index(tmp[i: i+7]))
    print(code)
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

    if (odd * 3 + even + verify) % 10 == 0:
        result = even + odd + verify
    else:
        result = 0

    print('#{} {}'.format(tc, result))