import sys
sys.stdin = open('선반.txt')

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    # B 이상 의 탑 중에서 작은 탑 - B
    tmp = set()

    for i in range(1, 1 << len(H)):
        sum_H = 0
        for j in range(len(H)+1):
            if i & (1 << j):
                sum_H += H[j]

        if sum_H >= B:
            tmp.add(sum_H)

    print('#{} {}'.format(tc, min(tmp) - B))

    #재귀로 풀어야 테스트케이스 많아졌을때 돌아감.


def calc(n, k, cursum):
    global ans
    if cursum >= B:
        if ans > cursum:
            ans = cursum
            return

def powerset(n, k, cursum):
    if ans < cursum: return # 가지치기

    if n == k:
        calc(n, k, cursum)
    else:
        A[k] = 1
        powerset(n, k+1, cursum + h[k])
        A[k] = 0
        powerset(n, k+1, cursum)

