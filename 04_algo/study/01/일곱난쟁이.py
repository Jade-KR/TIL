import sys
sys.stdin = open('일곱난쟁이.txt')

def comb(dep=0):
    global check
    if check == 1:
        return
    if len(arr) == n:
        tmp = 0
        for i in range(n):
            tmp += arr[i]
        if tmp == 100:
            check = 1
            for j in sorted(arr):
                print(j)
        return

    if dep == len(info):
        return

    for k in range(dep, len(info)):
        arr.append(info[k])
        comb(k+1)
        arr.pop()

info = []
for _ in range(9):
    info.append(int(input()))

check = 0
n = 7
arr = []
comb()