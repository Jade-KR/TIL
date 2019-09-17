N = 10
total = 0
count = 0
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def printSet(n, sum):
    global count
    if sum == 10:
        for i in range(n):
            if A[i] == 1:
                print(data[i], end=' ')
        print()
def powerset(n, k, sum):
    global total
    if sum > 10: return
    total += 1
    if n == k:
        printSet(n, sum)
    else:
        A[k] = 1
        powerset(n, k + 1, sum + data[k])
        A[k] = 0
        powerset(n, k + 1, sum)

powerset(N, 0, 0)
print('호출회수 : {}'.format(total))
