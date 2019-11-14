def comb(dep=0):
    if len(arr) == 3:
        print(arr)
        return
    if dep == len(a):
        return
    for i in range(dep, len(a)):
        arr.append(a[i])
        comb(i+1)
        arr.pop()

a = [1, 2, 3, 4, 5]
arr= []
comb()