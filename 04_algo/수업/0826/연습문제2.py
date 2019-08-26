count = 0
N = 10
A = [0 for _ in range(N)] # 원소의 포함여부 저장 (0, 1)
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def printSet(n):
    sum_a = 0
    for i in range(n): # 각 부분 배열의 원소 출력
        if A[i] == 1: # A[i]가 1이면 포함된 것이므로 출력.
            sum_a += data[i]

    if sum_a == 10:
        for i in range(n):  # 각 부분 배열의 원소 출력
            if A[i] == 1:  # A[i]가 1이면 포함된 것이므로 출력.
                print('{}'.format(data[i]), end=",")
        print()

def powerset(k, sum=0):     # n: 원소의 갯수, k: 현재 depth
    if N == k:          # Basis part
        printSet(N)
    elif sum == 10:
        printSet(N)
    else:
        A[k] = 1
        if sum+data[k] > 10:
            A[k] = 0
            return
        powerset(k + 1, sum + data[k]) # 다음 요소 포함 여부 결정
        A[k] = 0
        powerset(k + 1, sum) # 다음 요소 포함 여부 결정

powerset(0)