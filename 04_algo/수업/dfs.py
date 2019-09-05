'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(v):
    visited[v] = 1
    print(v, end=" ")

    for w in range(n+1):
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w)



n, m = map(int, input().split())

line = list(map(int, input().split()))

adj = [[0 for _ in range(n+1)] for _ in range(n+1)]

visited = [0 for i in range(n+1)]

for i in range(0, len(line), 2):
    adj[line[i]][line[i+1]] = 1
    adj[line[i+1]][line[i]] = 1

for i in range(n+1):
    print("{} {}".format(i, adj[i]))

dfs(1)