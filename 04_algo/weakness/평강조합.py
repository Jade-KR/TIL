def com(dep=0):
    if len(arr) == n:
        print(arr)
        return
    if dep == len(a):
        return
    for i in range(dep, len(a)):
        arr.append(a[i])
        com(i+1)
        arr.pop()

a = [1, 2, 3, 4, 5]
arr = []
n = 3
com()


def comb(dep=0):
    if len(arr) == n:
        print(arr)
        return
    if dep == len(a):
        return
    for i in range(dep, len(a)):
        arr.append(a[i])
        comb(i+1)
        arr.pop()