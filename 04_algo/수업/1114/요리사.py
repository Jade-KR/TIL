import sys
sys.stdin = open('요리사.txt')

def powerset(n, dep):
    global f1, f2, min_c
    if dep == n:
        f1 = []
        f2 = []
        for i in range(N):
            if A[i] == 1:
                f1.append(arr[i])
            if A[i] == 0:
                f2.append(arr[i])
        if len(f1) == N//2 and len(f2) == N//2:
            r1 = 0
            r2 = 0
            for i in range(N//2):
                for j in range(i, N//2):
                    if i != j:
                        r1 += igt[f1[i]-1][f1[j]-1] + igt[f1[j]-1][f1[i]-1]
                        r2 += igt[f2[i]-1][f2[j]-1] + igt[f2[j]-1][f2[i]-1]
            if r1 != 0 and r2 != 0:
                if min_c > abs(r1 - r2):
                    min_c = abs(r1 - r2)

    else:
        A[dep] = 1
        powerset(n, dep+1)
        A[dep] = 0
        powerset(n, dep+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    igt = [list(map(int, input().split())) for _ in range(N)]
    min_c = 987654321
    tmp = 987654321

    arr = [i+1 for i in range(N)]
    A = [0 for _ in range(N)]

    powerset(N, 0)
    print('#{} {}'.format(tc, min_c))