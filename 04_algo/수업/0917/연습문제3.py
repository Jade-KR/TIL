N = 10
total = 0
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def printSet(n):
    sum_a = 0
    for i in range(n):
        if A[i] == 1:
            sum_a += data[i]
    if sum_a == 10:
        for i in range(n):
            if A[i] == 1:
                print(data[i], end=" ")
        print()
def powerset(n, k):
    if n == k:
        printSet(n)
    else:
        A[k] = 1
        powerset(n, k + 1)
        A[k] = 0
        powerset(n, k + 1)

powerset(N, 0)
