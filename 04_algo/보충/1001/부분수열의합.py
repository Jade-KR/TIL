import sys
sys.stdin= open('부분수열의합.txt')

def power(dep=0, s=0):
    global cnt
    if s > K:
        return
    if s == K:
        cnt += 1
        return
    if dep == N:
        return
    power(dep+1, s+A[dep])
    power(dep+1, s)


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    power()
    print('#{} {}'.format(tc, cnt))