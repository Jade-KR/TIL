def perm2(arr=[]):
    if len(arr) == 3:
        print(arr)
        return
    for i in range(3):
        if not vl[i]:
            arr.append(data[i])
            vl[i]=1
            perm2(arr)
            arr.pop()
            vl[i]=0

data = [5, 3, 2]
vl = [0, 0, 0]
perm2()