def perm(arr=[]):
    global flag, result, fp1, fp2
    if len(arr) == len(vl):
        for x in arr:
            fp1.append(p1[x])
            fp2.append(p2[x])

        for j in range(len(p1)-2):
            if flag == 1:
                break
            for k in range(1):
                if fp1[k+j] == fp1[k+1+j] == fp1[k+2+j] or fp1[k+j] == fp1[k+1+j]-1 == fp1[k+2+j]-2:
                    result = 1
                    flag = 1
                    break
                elif fp2[k+j] == fp2[k+1+j] == fp2[k+2+j] or fp2[k+j] == fp2[k+1+j]-1 == fp2[k+2+j]-2:
                    result = 2
                    flag = 1
                    break
        fp1 = []
        fp2 = []
    for l in range(len(vl)):
        if not vl[l]:
            arr.append(l)
            vl[l] = 1
            perm()
            arr.pop()
            vl[l] = 0


import sys
sys.stdin = open('베이비진.txt')

T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    fp1 = []
    fp2 = []
    p1 = []
    p2 = []
    flag = 0
    result = 0
    for i in range(len(data)):
        if flag == 1:
            break
        if i % 2 == 1:
            p2.append(data[i])
        else:
            p1.append(data[i])

        if len(p1) >= 3 and len(p1) == len(p2):
            vl = [0]*len(p1)
            perm()

    print('#{} {}'.format(tc, result))
