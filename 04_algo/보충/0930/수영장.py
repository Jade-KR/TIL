import sys
sys.stdin = open('수영장.txt')

def cmp(a):
    if D*a > M*a:
        return M
    else:
        return D


T = int(input())
for tc in range(1, T+1):
    D, M, M3, Y = map(int, input().split())
    plan = list(map(int, input().split()))
    visited = [0]*12
    check = 0
    Ma = 987654321
    Mb = 0
    Mc = 0
    p = 0
    min_p = 987654321
    tmp = 0
    for i in plan:
        if i:
            tmp += i*D
    if min_p > tmp:
        min_p = tmp

    tmp = 0
    for i in plan:
        if i:
            tmp += M
    if min_p > tmp:
        min_p = tmp

    for i in range(len(plan) - 2):
        for k in range(i, len(plan), 3):
            tmp = 0
            check = 0
            for j in range(3):
                if plan[j]:
                    check += 1
                    visited[j] = 1
            if check:
                tmp += M3
        if min_p > tmp:
            min_p = tmp
            tmp = 0

    if min_p > Y:
        min_p = Y
    print('#{} {}'.format(tc, min_p))

''''
1일치 가격이 1달치 가격을 몇일 째에 넘어서는지 체크

1년치 비용 체크
1달짜리와 1일치로 체크하고 최소비용 저장 3달치로 완전탐색 하고 체크 한곳 0으로 바꾼 후
1달짜리와 1일치로 체크하고 최소비용 저장
1달치 or 1일치 중 값이 적은 것으로 비용 저장

'''