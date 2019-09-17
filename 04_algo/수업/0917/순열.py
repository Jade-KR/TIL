def babygin():
    global flag
    check = 0

    if data[0] == data[1] and data[1] == data[2]: check += 1
    if data[3] == data[4] and data[4] == data[5]: check += 1

    if data[0] + 1 == data[1] and data[1] +1 == data[2]: check += 1
    if data[3] + 1 == data[4] and data[4] +1 == data[5]: check += 1

    if check == 2:
        flag = 1
        return


def perm(arr=[]):
    if flag == 1: return
    if len(arr) == 6:
        babygin()
        # for j in arr:
        #     print(data[j], end='')
        # print()
        return
    for i in range(6):
        if not vl[i]:
            arr.append(i)
            vl[i] = 1
            perm(arr)
            arr.pop()
            vl[i] = 0


data = [0, 5, 4, 0, 6, 0]
vl = [0, 0, 0, 0, 0 ,0]
flag = 0
perm()