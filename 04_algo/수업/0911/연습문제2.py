import sys
sys.stdin = open('연습문제2.txt')

data = input()
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
        tmp += bin(ord(i)-ord('A')+10)[2:]

print(tmp)

for i in range(0, len(tmp), 7):
    print(int(tmp[i: i+7], 2))

# 2진수로 바꾸고(자리수 4자리수로 맞춰야함) 7개씩 끊어서 10진수로 변환