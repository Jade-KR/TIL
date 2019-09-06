def perm2(arr=[]):
    if len(arr) == N:
        print(arr)
        return
    for i in range(N):
        if not vl[i]:
            arr.append(i)
            vl[i]=1
            perm2(arr)
            arr.pop()
            vl[i]=0



import sys
sys.stdin = open('최적경로.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    cp = (data[0], data[1])
    home = (data[2], data[3])
    cs = data[4::]

    vl = [0 for _ in range(N)]
    perm2()