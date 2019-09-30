def backtrack(n, cost):
    global ans
    if cost >= ans: return
    if n >= 13:
        ans = min(ans, cost)
    else:
        if arr[n]:
            backtrack(n + 1, cost + day * arr[n])   # 1일 이용권
            backtrack(n + 1, cost + month)          # 한달 이용권
            backtrack(n + 3, cost + quarter)        # 3개월 이용권
            backtrack(n + 12, cost + year)          # 1년 이용권
        else:
            backtrack(n + 1, cost)                  # 0 일때

import sys
sys.stdin = open("수영장.txt")
T = int(input())
for tc in range(1, T + 1):
    day, month, quarter, year = map(int, input().split())
    arr = [0] + list(map(int, input().split()))  # 1월 ~ 12월
    ans = year

    backtrack(1, 0)

    print('#{} {}'.format(tc, ans))
