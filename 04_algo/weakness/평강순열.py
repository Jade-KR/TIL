def perm2(arr1=[], arr2=[]):
    for i in range(3):
        if not vl[i]:
            arr1.append(data[i])
            vl[i]=1
            perm2(arr1, arr2)
            arr1.pop()
            vl[i]=0


data = [5, 3, 2]
vl = [0, 0, 0]
perm2()