def MST_Prim(info, r):
    total = 0
    u = 0
    D[u] = 0

    for i in range(V+1):
        min = 987654321
        for v in range(V+1):
            if visit[v] == 0 and min > D[v]:
                min = D[v]
                u = v

        visit[u] = 1
        total += adj[pi[u]][u]

        for v in range(V+1):
            if adj[u][v] != 0 and visit[v] == 0 and adj[u][v] < D[v]:
                D[v] = adj[u][v]
                pi[v] = u

    return total


import sys
sys.stdin = open('최소신장트리.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(E)]
    adj = [[0 for _ in range(V+1)] for _ in range(V+1)]
    D = [987654321]*(V+1)
    pi = list(range(V+1))
    visit = [0] * (V+1)

    for i in range(E):
        adj[info[i][0]][info[i][1]] = info[i][2]
        adj[info[i][1]][info[i][0]] = info[i][2]

    print('#{} '.format(tc), end='')
    print(MST_Prim(info, 0))
