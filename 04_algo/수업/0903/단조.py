import sys
sys.stdin = open('단조.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    tmp = []
    lis = []
    a = 2
    result = -1

    for i in range(len(data)):
        for j in range(1+i, len(data)):
            tmp.append(data[i]*data[j])



    for i in tmp:
        tmp2 = str(i)
        chk = 0
        for j in range(len(tmp2)-1):
            if tmp2[j] > tmp2[j+1]:
                chk = 1
                break
        if not chk:
            result = i


    print('#{} {}'.format(tc, result))