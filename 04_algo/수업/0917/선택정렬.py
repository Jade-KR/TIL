A = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]

def recselectionsort(A, s, e):
    n = len(A)
    if s == e:
        return
    else:
        mini = s
        for i in range(s+1, e, 1):
            if A[i] < A[mini]:
                mini = i

        A[s], A[mini] = A[mini], A[s]
        recselectionsort(A, s+1, e)


def SelectionSort(A):
    n = len(A)
    for i in range(0, n-1):
        mini = i
        for j in range(i+1, n):
            if A[j] < A[mini]:
                mini = j
        A[i], A[mini] = A[mini], A[i]

# SelectionSort(A)
recselectionsort(A, 0, 10)
print(A)