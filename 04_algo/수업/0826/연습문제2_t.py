count = 0
N = 10
A = [0 for _ in range(N)] # 원소의 포함여부 저장 (0, 1)
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
def printSet(n, sum):
    global count
    if sum == 10:
        count += 1
        print("%d : " % count, end="")
        for i in range(n):
            if A[i] == 1:
                print("%d " % data[i], end="")
        print()

def powerset(n, k, sum):
    global total
    if sum > 10:
        return
    total += 1
    if n == k:
        printSet(n, sum)
    else:
        A[k] = 1
        powerset(n, k +1, sum + data[k])
        A[k] = 0
        powerset(n, k+1, sum)

powerset(N, 0, 0)
print("호출회수 : {}".format(total))