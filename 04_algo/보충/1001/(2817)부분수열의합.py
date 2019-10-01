import sys
sys.stdin = open("(2817)부분수열의합_input.txt")

def powerset(n, k, cursum):
    global cnt
    if cursum > SUM: return

    if n == k:
        if cursum == SUM: cnt += 1
    else:
        A[k] = 1
        powerset(n, k+1, cursum + data[k])
        A[k] = 0
        powerset(n, k+1, cursum)

T = int(input())
for tc in range(T):
    N, SUM = map(int, input().split())
    data = list(map(int, input().split()))
    A = [0] * N
    cnt =0

    powerset(N, 0, 0)
    print("#{} {}".format(tc+1, cnt))