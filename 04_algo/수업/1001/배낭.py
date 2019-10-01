def power(arr, kg):
    global ans
    if kg > W:
        return
    if kg <= W:
        tmp = 0
        for k in arr:
            tmp += k
        if ans < tmp:
            ans = tmp

    for i in range(n):
        if vl[i] == 0:
            arr.append(value[i])
            vl[i] = 1
            power(arr, kg+weight[i])
            arr.pop()
            vl[i] = 0


W = 10
n = 4
weight = [5, 4, 6, 3]
value= [10, 40, 30, 50]
vl = [0] * n
ans = 0
arr = []
power(arr, 0)
print(ans)