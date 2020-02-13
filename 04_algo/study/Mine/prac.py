import sys
sys.stdin = open("prac.txt")

def comb(dep=0):
    global ans
    if len(arr) == c:
        B = []
        for p in A:
            B.append(p)
        for k in arr:
            B.remove(k)

        cmp1 = 0
        cmp2 = 0
        for a in range(N//2):
            for b in range(N//2):
                if a != b:
                    cmp1 += data[arr[a]][arr[b]] + data[arr[b]][arr[a]]
                    cmp2 += data[B[a]][B[b]] + data[B[b]][B[a]]
        if ans > abs(cmp1 - cmp2):
            ans = abs(cmp1 - cmp2)
        return
    if dep >= len(A):
        return
    for i in range(dep, len(A)):
        arr.append(A[i])
        comb(i+1)
        arr.pop()



N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

A = [i for i in range(N)]
c = len(A)//2
arr = []
ans = 9876545334
comb()

print(ans)