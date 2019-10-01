import sys
sys.stdin = open('거스름돈.txt')

def spare(money, cnt):
    global ans

    if ans < cnt or money < 0: return

    if money == 0:
        if ans > cnt: ans = cnt
    else:
        for i in range(n):
            spare(money - data[i], cnt+1)
m = int(input())
n = int(input())
data = list(map(int, input().split()))
ans = 987654321
spare(m, 0)
print(ans)