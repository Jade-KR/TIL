import sys
sys.stdin = open('벌꿀채취.txt')

def powerset(dep, arr):
    global max_t
    if dep == M:
        tmp = 0
        for i in range(len(cmp)):
            if cmp[i] == 1:
                tmp += arr[i]
        if tmp <= C:
            tmp = 0
            for i in range(len(cmp)):
                if cmp[i] == 1:
                    tmp += arr[i] ** 2
            if tmp > max_t:
                max_t = tmp
    else:
        cmp[dep] = 1
        powerset(dep+1, arr)
        cmp[dep] = 0
        powerset(dep+1, arr)

def check(arr):
    global max_t, cmp
    tmp = 0
    result = 0
    max_t = -9876754
    cmp = [0]*M
    for q in arr:
        tmp += q
    if tmp <= C:
        for q in arr:
            result += q**2
        return result
    else:
        powerset(0, arr)
        result = max_t
        return result

T = int(input())

for tc in range(1, T+1):
    N, M, C =  map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    ans = -987654321

    for i in range(N):
        for j in range(N):
            if j+M-1 >= N:
                break
            A = []
            ready = 0
            for k in range(M):
                visited[i][j+k] = 1
                A.append(data[i][j+k])

            for a in range(N):
                if a < i:
                    continue
                for b in range(N):
                    if a == i and b <= j or visited[a][b]:
                        continue
                    if b+M-1 >= N:
                        break
                    ready = 0
                    B = []
                    for c in range(M):
                        B.append(data[a][b+c])

                    ready += check(A)
                    ready += check(B)

                    if ans < ready:
                        ans = ready

    print('#{} {}'.format(tc, ans))