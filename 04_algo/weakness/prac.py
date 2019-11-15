def perm(arr=[]):
    if len(arr) == 4:
        print(arr)
    for i in range(4):
        if vl[i] == 0:
            vl[i] = 1
            arr.append(data[i])
            perm(arr)
            arr.pop()
            vl[i] = 0


data = [1, 2, 3, 4]
vl = [0]*4
perm()