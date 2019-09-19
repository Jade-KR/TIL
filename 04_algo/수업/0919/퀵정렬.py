def partition(A, L, r):
    p = A[L]
    i = L
    j = r
    while i < j:
        while A[i] <= p:
            i += 1
            if i == r:
                break

        while A[j] >= p:
            j -= 1
            if j == L:
                break

        if i < j:
            A[i], A[j] = A[j], A[i]

    A[L], A[j] = A[j], A[L]
    return j

def quicksort(A, L, r):
    if L < r:
        p = partition(A, L, r)
        quicksort(A, L, p-1)
        quicksort(A, p+1, r)

import sys
sys.stdin = open('퀵정렬.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    quicksort(A, 0, len(A)-1)

    print('#{} {}'.format(tc, A[N//2]))