import sys
sys.stdin = open('게리맨더링.txt')

def dfs(w):
    global flag, cnt, check
    visited[w] = 1
    for k in range(1, N+1):
        if adj[w][k] == 0 or visited[k] == 1:
            continue
        visited[k] = 1
        dfs(k)
    if flag == 1:
        return
    cnt = 0
    for i in range(N+1):
        if visited[i] == 1:
            cnt += 1
    if cnt == N+1:
        flag = 1
        check = 1
        return

def powerset(n, dep):
    global visited, flag, cnt, check, result, validator
    if n == dep:
        g1 = []
        g2 = []
        for i in range(n):
            if A[i] == 1:
                g1.append(arr[i])
            else:
                g2.append(arr[i])
        # validator = 0
        # for i in g1:
        #     for j in range(1, info[i-1][0]+1):
        #         if info[i-1][j] in g2:
        #             validator = 1
        #
        # if validator == 1:
        if len(g1) != 0 and len(g1) != N:
            if g1:
                visited = [1] * (N + 1)
                flag = 0
                cnt = 0
                check = 0
                for i in range(len(g1)):
                    visited[g1[i]] = 0
                dfs(g1[i])

                if check == 1:
                    if g2:
                        visited = [1] * (N + 1)
                        flag = 0
                        cnt = 0
                        check = 0
                        for i in range(len(g2)):
                            visited[g2[i]] = 0
                        dfs(g2[i])


                        if check == 1:
                            sum_g1 = 0
                            sum_g2 = 0
                            for p in g1:
                                sum_g1 += people[p-1]
                            for p in g2:
                                sum_g2 += people[p-1]
                            tmp = abs(sum_g1-sum_g2)
                            if result > tmp:
                                result = tmp

    else:
        A[dep] = 1
        powerset(n, dep+1)
        A[dep] = 0
        powerset(n, dep+1)


N = int(input())
people = list(map(int, input().split()))
info = [list(map(int, input().split())) for _ in range(N)]
adj = [[0] * (N+1) for _ in range(N+1)]
cnt = 0
check = 0
result = 98765124
validator = 0
for i in range(N):
    for j in range(1, len(info[i])):
        adj[i+1][info[i][j]] = 1

arr = [i+1 for i in range(N)]
A = [0] * N

powerset(N, 0)

if result == 98765124:
    result = -1
print(result)