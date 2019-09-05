def dfs(s):
    global flag
    if s == goal:
        flag = 1
        return
    visited[s] = 1

    for i in range(1, V+1):
        if adj[s][i] == 1 and visited[i] == 0:
            dfs(i)


import sys
sys.stdin = open('그래프경로.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    flag = 0
    adj = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for i in range(E):
        s_node, e_node = map(int, input().split())
        adj[s_node][e_node] = 1

    start, goal = map(int, input().split())
    dfs(start)

    print("#{} {}".format(tc, flag))