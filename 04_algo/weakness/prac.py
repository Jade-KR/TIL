import sys
sys.stdin = open('prac.txt')

def dfs(v):
    visited[v] = 1
    for w in range(1, V+1):
        if adj[v][w] == 1 and visited[v][w] == 0:


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    visited = [[0]*(V+1) for _ in range(V+1)]

    for i in range(E):
        adj[info[i][0]][info[i][1]] = 1

    dfs(S)

