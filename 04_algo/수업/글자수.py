import sys
sys.stdin = open('글자수.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    final_cnt = 0
    tmp = []
    for j in range(len(str1)):
        cnt = 0
        for k in range(len(str2)):
            if str1[j] == str2[k]:
                cnt += 1

        tmp.append(cnt)

    sup = tmp[0]
    for i in tmp:
        if sup < i:
            sup = i
    print('#{} {}'.format(tc, sup))