import sys
sys.stdin = open('베이비진.txt')

T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    p1 = []
    p2 = []
    flag = 0
    result = 0
    for i in range(len(data)):
        if flag == 1:
            break
        if i % 2 == 1:
            p2.append(data[i])
            p2 = sorted(p2)
        else:
            p1.append(data[i])
            p1 = sorted(p1)

        if len(p1) >= 3 and len(p1) == len(p2):
            for j in range(len(p1)-2):
                if flag == 1:
                    break
                for k in range(1):
                    if p1[k+j] == p1[k+1+j] == p1[k+2+j] or p1[k+j] == p1[k+1+j]-1 == p1[k+2+j]-2:
                        result = 1
                        flag = 1
                        break
                    elif p2[k+j] == p2[k+1+j] == p2[k+2+j] or p2[k+j] == p2[k+1+j]-1 == p2[k+2+j]-2:
                        result = 2
                        flag = 1
                        break

    print('#{} {}'.format(tc, result))
