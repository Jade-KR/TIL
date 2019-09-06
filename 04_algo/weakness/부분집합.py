count = 0
N = 3
A = [0 for _ in range(N)] # 원소의 포함여부 저장 (0, 1)
data = [1, 2, 3]
total = 0
def printSet(n):
    global count
    count += 1
    print("%d : " % (count), end="") #생성되는 배열의 갯수 출력
    for i in range(n): # 각 부분 배열의 원소 출력
        if A[i] == 1: # A[i]가 1이면 포함된 것이므로 출력.
            print("%d " % data[i], end="")
    print()

def powerset(n, k):     # n: 원소의 갯수, k: 현재 depth
    if n == k:          # Basis part
        printSet(n)
    else:
        A[k] = 1
        powerset(n, k + 1) # 다음 요소 포함 여부 결정
        A[k] = 0
        powerset(n, k + 1) # 다음 요소 포함 여부 결정

powerset(N, 0)