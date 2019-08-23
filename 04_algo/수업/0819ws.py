import sys
sys.stdin = open('0819.txt')


T = 10
for tc in range(1, T+1):
    cnt = 0
    box =[]
    length = int(input())
    box.append(input())
    for i in range(len(box[0]) - 1):
        box.append(input())
    for i in range(len(box[0])):
        for j in range(len(box[0]) - length + 1):
            cmp = box[i][j:j+length]
            if cmp == cmp[::-1]:
                cnt += 1

    for i in range(len(box[0])-length+1):
        for j in range(len(box[0])):
            cmp =''
            for l in range(length):
                cmp += box[i+l][j]
            if cmp == cmp[::-1]:
                cnt += 1

    print('#{} {}'.format(tc, cnt))

'''
행을 확인하면서 회문이면 cnt +1, 열 확인하면서 회문이면 cnt +1
확인할때 반복 횟수 = 전체 길이 - length 길이 - 1

'''