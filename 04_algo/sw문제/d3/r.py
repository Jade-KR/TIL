import sys
sys.stdin = open('r.txt', 'r', encoding='utf-8')

T = 10
for tc in range(1, T+1):
    t = int(input())
    st = input()
    sample = input()
    cnt = 0

    for i in range(len(sample)-len(st) + 1):
        tmp = ''
        for j in range(len(st)):
            tmp += sample[i+j]
            if st == tmp:
                cnt += 1

    print('#{} {}'.format(tc, cnt))