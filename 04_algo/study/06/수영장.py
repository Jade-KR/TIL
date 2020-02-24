import sys
sys.stdin = open('수영장.txt')

def check(m, money):
    global ans

    if m >= 12:
        if ans > money:
            ans = money
        return

    if plan[m]:
        for i in range(3):
            cost = costs[i]
            if i == 0:
                check(m+1, money + cost*plan[m])
            elif i == 1:
                check(m+1, money + cost)
            else:
                check(m+3, money + cost)
    else:
        check(m+1, money)

T = int(input())

for tc in range(1, T+1):
    costs = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    ans = costs[3]
    check(0, 0)
    print('#{} {}'.format(tc, ans))


