import sys
sys.stdin = open('정식이.txt')

T = int(input())
for tc in range(1, T+1):
    two = list(input())
    three = list(input())
    ans2 = 0
    ans3 = 0
    result= 0

    for i in range(len(two)):
        if two[i] == '0':
            two[i] = '1'
        elif two[i] == '1':
            two[i] = '0'
        tmp2 = ''
        for k in two:
            tmp2 += k
        ans2 = int(tmp2, 2)
        for j in range(len(three)):
            if j == i:
                continue
            if three[j] == '2':
                three[j] = '1'
            elif three[j] == '1':
                three[j] = '2'
            tmp3 = ''
            for k in three:
                tmp3 += k
            ans3 = int(tmp3, 3)
            if ans2 == ans3:
                result = ans2

    print(result)

