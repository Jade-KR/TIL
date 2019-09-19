def partition(A, L, r):
    p = A[L]
    i = L
    j = r
    while i < j:
        while A[i] <= p:
            if i == r:
                break
            i += 1
        while A[j] >= p:
            if j == L:
                break
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]

    A[L], A[j] = A[j], A[L]
    return j

def quicksort(A, L, r):
    if L < r:
        p = partition(A, L, r)
        quicksort(A, L, p-1)
        quicksort(A, p+1, r)

A = [12, 12, 42, 342, 34, 12, 54, 64, 12, 34]
quicksort(A, 0, len(A)-1)

print(A)

