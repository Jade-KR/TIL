import sys
sys.stdin = open('회문2.txt')

T = 10
for tc in range(1, T+1):
    n = int(input())
    box = []
    length = []
    for i in range(100):
        box.append(input())
# 슬라이싱해서 회문이 되는지 비교하고 맞으면 길이 append
    for i in range(100):
        for j in range(100):
            for k in range(1,100-j+1):
                cmp = box[i][j:j+k]
                if cmp == cmp[::-1]:
                    length.append(len(cmp))
    for i in range(100):
        for j in range(100):
            cmp =''
            for l in range(100-i):
                cmp += box[l+i][j]
                if cmp == cmp[::-1]:
                    length.append(len(cmp))

    sup_length = 1
    for i in length:
        if sup_length < i:
            sup_length = i

    print('#{} {}'.format(tc, sup_length))