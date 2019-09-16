import sys
sys.stdin = open('암호코드스캔.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    cmp = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    cmp2 = ['', '', '', '', '', '', '', '', '', '', '']
    for i in range(len(cmp)):
        for j in range(7):
            cmp2[i] += cmp[i][j] * (N // 100)

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

    f_code = []
    for l in range(len(pwd)):
        cnt = len(pwd[l])
        for i in range(len(pwd[l])-1, -1, -1):
            if pwd[l][i] == '1':
                break
            cnt -= 1
        key = cnt-56*len(pwd)
        code = ''
        for o in range(key, len(pwd[l]), 7):
            if pwd[l][o: o + 7] in cmp:
                code += str(cmp.index(pwd[l][o: o+7]))
                if len(code) == 8:
                    f_code.append(code)
    print(f_code)
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

    # print('#{} {}'.format(tc, result))